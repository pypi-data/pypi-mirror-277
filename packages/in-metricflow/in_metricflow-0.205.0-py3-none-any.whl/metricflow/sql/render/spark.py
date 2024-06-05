from typing import Collection
from datetime import datetime
from dateutil.parser import parse
from dbt_semantic_interfaces.enum_extension import assert_values_exhausted
from dbt_semantic_interfaces.type_enums.date_part import DatePart
from dbt_semantic_interfaces.type_enums.time_granularity import TimeGranularity
from metricflow.sql.render.expr_renderer import (
    DefaultSqlExpressionRenderer,
    SqlExpressionRenderer,
    SqlExpressionRenderResult,
)
from metricflow.sql.render.sql_plan_renderer import DefaultSqlQueryPlanRenderer
from metricflow.sql.sql_bind_parameters import SqlBindParameters
from metricflow.sql.sql_exprs import (
    SqlBetweenExpression,
    SqlGenerateUuidExpression,
    SqlPercentileExpression,
    SqlPercentileFunctionType,
    SqlSubtractTimeIntervalExpression,
)


class SparkSqlExpressionRenderer(DefaultSqlExpressionRenderer):
    """Expression renderer for the Spark SQL engine."""

    @property
    def supported_percentile_function_types(self) -> Collection[SqlPercentileFunctionType]:
        return {
            SqlPercentileFunctionType.APPROXIMATE_CONTINUOUS,
        }

    def visit_generate_uuid_expr(self, node: SqlGenerateUuidExpression) -> SqlExpressionRenderResult:
        return SqlExpressionRenderResult(
            sql="uuid()",
            bind_parameters=SqlBindParameters(),
        )

    def visit_time_delta_expr(self, node: SqlSubtractTimeIntervalExpression) -> SqlExpressionRenderResult:
        """Render time delta for Spark SQL."""
        arg_rendered = node.arg.accept(self)

        count = node.count
        granularity = node.granularity
        if granularity == TimeGranularity.QUARTER:
            granularity = TimeGranularity.MONTH
            count *= 3
        return SqlExpressionRenderResult(
            sql=f"date_sub({arg_rendered.sql}, {count})",
            bind_parameters=arg_rendered.bind_parameters,
        )

    def visit_percentile_expr(self, node: SqlPercentileExpression) -> SqlExpressionRenderResult:
        """Render a percentile expression for Spark SQL."""
        arg_rendered = self.render_sql_expr(node.order_by_arg)
        params = arg_rendered.bind_parameters
        percentile = node.percentile_args.percentile

        if node.percentile_args.function_type is SqlPercentileFunctionType.APPROXIMATE_CONTINUOUS:
            return SqlExpressionRenderResult(
                sql=f"percentile_approx({arg_rendered.sql}, {percentile})",
                bind_parameters=params,
            )
        else:
            raise RuntimeError(
                "Only approximate continuous percentile aggregates are supported for Spark SQL."
            )

    def visit_between_expr(self, node: SqlBetweenExpression) -> SqlExpressionRenderResult:
        """Render a between expression for Spark SQL."""
        rendered_column_arg = self.render_sql_expr(node.column_arg)
        rendered_start_expr = self.render_sql_expr(node.start_expr)
        rendered_end_expr = self.render_sql_expr(node.end_expr)

        bind_parameters = SqlBindParameters()
        bind_parameters = bind_parameters.combine(rendered_column_arg.bind_parameters)
        bind_parameters = bind_parameters.combine(rendered_start_expr.bind_parameters)
        bind_parameters = bind_parameters.combine(rendered_end_expr.bind_parameters)

        # Handle timestamp literals differently.
        if parse(rendered_start_expr.sql):
            sql = f"{rendered_column_arg.sql} BETWEEN TIMESTAMP '{rendered_start_expr.sql}' AND TIMESTAMP '{rendered_end_expr.sql}'"
        else:
            sql = f"{rendered_column_arg.sql} BETWEEN {rendered_start_expr.sql} AND {rendered_end_expr.sql}"

        return SqlExpressionRenderResult(
            sql=sql,
            bind_parameters=bind_parameters,
        )

    def render_date_part(self, date_part: DatePart) -> str:
        """Render DATE PART for an EXTRACT expression."""
        if date_part is DatePart.DOW:
            return "DAYOFWEEK"

        return date_part.value


class SparkSqlQueryPlanRenderer(DefaultSqlQueryPlanRenderer):
    """Plan renderer for the Spark SQL engine."""

    EXPR_RENDERER = SparkSqlExpressionRenderer()

    @property
    def expr_renderer(self) -> SqlExpressionRenderer:
        return self.EXPR_RENDERER
