from __future__ import annotations

import logging
import pathlib
from logging.handlers import TimedRotatingFileHandler
from typing import Dict, Optional

from dbt_semantic_interfaces.protocols.semantic_manifest import SemanticManifest

from metricflow.cli.dbt_connectors.adapter_backed_client import AdapterBackedSqlClient
from metricflow.cli.dbt_connectors.dbt_config_accessor import dbtArtifacts, dbtProjectMetadata
from metricflow.engine.metricflow_engine import MetricFlowEngine
from metricflow.model.semantic_manifest_lookup import SemanticManifestLookup
from metricflow.protocols.sql_client import SqlClient

from dbt.cli.main import dbtRunner

logger = logging.getLogger(__name__)


class APIContext:
    """Context for MetricFlow CLI."""

    def __init__(self, semantic_json, adapter=None, dbt_project=None) -> None:
        """Initialize the CLI context for executing commands.

        The dbt_artifacts construct must be loaded in order for logging configuration to work correctly.
        """
        self.verbose = False
        self.adapter = adapter
        self.semantic_json = semantic_json
        # self._dbt_project_metadata: dbtProjectMetadata = dbtProjectMetadata.load_from_project_path(dbt_project)
        self._dbt_artifacts: Optional[dbtArtifacts] = None
        self._mf: Optional[MetricFlowEngine] = None
        self._sql_client: Optional[SqlClient] = None
        self._semantic_manifest: Optional[SemanticManifest] = None
        self._semantic_manifest_lookup: Optional[SemanticManifestLookup] = None

        # Initialize dbt context, without this Trino adapter is not getting registered
        # TODO: Find a better way to do this
        dbtRunner().invoke(["-q", "debug"], project_dir=str("/"))


    @property
    def dbt_project_metadata(self) -> dbtProjectMetadata:
        """Property accessor for dbt project metadata, useful in cases where the full manifest load is not needed."""
        return None

    @property
    def dbt_artifacts(self) -> dbtArtifacts:
        """Property accessor for all dbt artifacts, used for powering the sql client (among other things)."""
        if self._dbt_artifacts is None:
            self._dbt_artifacts = dbtArtifacts.load_from_api_metadata(self.adapter, self.semantic_json)
        return self._dbt_artifacts

    @property
    def sql_client(self) -> SqlClient:
        """Property accessor for the sql_client class used in the CLI."""
        if self._sql_client is None:
            self._sql_client = AdapterBackedSqlClient(self.dbt_artifacts.adapter)

        return self._sql_client

    def run_health_checks(self) -> Dict[str, Dict[str, str]]:
        """Execute the DB health checks."""
        checks_to_run = [
            ("SELECT 1", lambda: self.sql_client.execute("SELECT 1")),
        ]

        results: Dict[str, Dict[str, str]] = {}

        for step, check in checks_to_run:
            status = "SUCCESS"
            err_string = ""
            try:
                resp = check()
                logger.info(f"Health Check Item {step}: succeeded" + f" with response {str(resp)}" if resp else None)
            except Exception as e:
                status = "FAIL"
                err_string = str(e)
                logger.error(f"Health Check Item {step}: failed with error {err_string}")

            results[f"{self.sql_client.sql_engine_type} - {step}"] = {
                "status": status,
                "error_message": err_string,
            }

        return results

    @property
    def new_mf(self) -> MetricFlowEngine:  # noqa: D
        if self._mf is None:
            self._mf = MetricFlowEngine(
                semantic_manifest_lookup=self.semantic_manifest_lookup,
                sql_client=self.sql_client, # Python Client
            )
        assert self._mf is not None
        return self._mf

    def _build_semantic_manifest_lookup(self) -> None:
        """Get the path to the models and create a corresponding SemanticManifestLookup."""
        self._semantic_manifest_lookup = SemanticManifestLookup(self.semantic_manifest) # Parsed semantic manifest

    def _build_semantic_manifest_lookup_with_api(self) -> None:
        """Get the path to the models and create a corresponding SemanticManifestLookup."""
        self._semantic_manifest_lookup = SemanticManifestLookup(self.semantic_manifest) # Parsed semantic manifest

    @property
    def semantic_manifest_lookup(self) -> SemanticManifestLookup:  # noqa: D
        if self._semantic_manifest_lookup is None:
            self._build_semantic_manifest_lookup()
        assert self._semantic_manifest_lookup is not None
        return self._semantic_manifest_lookup

    @property
    def semantic_manifest(self) -> SemanticManifest:
        """Retrieve the semantic manifest from the dbt project root."""
        return self.dbt_artifacts.semantic_manifest
