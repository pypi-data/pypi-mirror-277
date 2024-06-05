from __future__ import annotations

import dataclasses
import logging
from pathlib import Path
from typing import List, Type

from dbt.adapters.base.impl import BaseAdapter
from dbt.adapters.factory import get_adapter_by_type
from dbt.cli.main import dbtRunner
from dbt.config.profile import Profile
from dbt.config.project import Project
from dbt.config.runtime import load_profile, load_project
from dbt_semantic_interfaces.protocols.semantic_manifest import SemanticManifest
from typing_extensions import Self

from metricflow.errors.errors import ModelCreationException
from metricflow.mf_logging.pretty_print import mf_pformat
from metricflow.model.dbt_manifest_parser import parse_manifest_from_dbt_generated_manifest

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class dbtPaths:
    """Bundle of dbt configuration paths."""

    model_paths: List[str]
    seed_paths: List[str]
    target_path: str


@dataclasses.dataclass
class dbtProjectMetadata:
    """Container to access dbt project metadata such as dbt_project.yml and profiles.yml."""

    profile: Profile
    project: Project
    project_path: Path

# >>> from metricflow.cli.api_context import APIContext                                                                                                       >>> APIContext("/Users/jdhiman/Downloads/semantic_manifest.json","/Users/jdhiman/projects/inmetrics-prototype/in-dbt-examples/in-dbt-examples/src/metrics_example/","").sql_client
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "/Users/jdhiman/projects/inmetrics-prototype/metricflow/metricflow/cli/api_context.py", line 53, in sql_client
# self._sql_client = AdapterBackedSqlClient(self.dbt_artifacts.adapter)
# File "/Users/jdhiman/projects/inmetrics-prototype/metricflow/metricflow/cli/api_context.py", line 46, in dbt_artifacts
# self._dbt_artifacts = dbtArtifacts.load_from_api_metadata(self.adapter, self.semantic_path)
# File "/Users/jdhiman/projects/inmetrics-prototype/metricflow/metricflow/cli/dbt_connectors/dbt_config_accessor.py", line 112, in load_from_api_metadata
# adapter = get_adapter_by_type(load_profile("/Users/jdhiman/projects/inmetrics-prototype/in-dbt-examples/in-dbt-examples/src/metrics_example", {}).credentials.type)
# File "/Users/jdhiman/projects/inmetrics-prototype/metricflow/inmetrics_api/lib/python3.9/site-packages/dbt/adapters/factory.py", line 174, in get_adapter_by_type
# return FACTORY.lookup_adapter(adapter_type)
# File "/Users/jdhiman/projects/inmetrics-prototype/metricflow/inmetrics_api/lib/python3.9/site-packages/dbt/adapters/factory.py", line 102, in lookup_adapter
# return self.adapters[adapter_name]
# KeyError: 'trino'
# >>> from dbt.cli.main import dbtRunner
# >>> dbtRunner().invoke(["-q", "debug"], project_dir=str(project_path))
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: name 'project_path' is not defined
# >>> project_path="/Users/jdhiman/projects/inmetrics-prototype/in-dbt-examples/in-dbt-examples/src/metrics_example/"
# >>> dbtRunner().invoke(["-q", "debug"], project_dir=str(project_path))
#
# dbtRunnerResult(success=False, exception=None, result=False)
# >>>
# >>> project_path="/Users/jdhiman/projects/inmetrics-prototype/in-dbt-examples/in-dbt-examples/src/metrics_example/"
# >>> APIContext("/Users/jdhiman/Downloads/semantic_manifest.json","/Users/jdhiman/projects/inmetrics-prototype/in-dbt-examples/in-dbt-examples/src/metrics_example/","").sql_client
# ********
# <metricflow.cli.dbt_connectors.adapter_backed_client.AdapterBackedSqlClient object at 0x139b13af0>
# >>> APIContext("/Users/jdhiman/Downloads/semantic_manifest.json","/Users/jdhiman/projects/inmetrics-prototype/in-dbt-examples/in-dbt-examples/src/metrics_example/","").sql_client
    @classmethod
    def load_from_project_path(cls: Type[Self], project_path: Path) -> Self:
        """Loads all dbt artifacts for the project associated with the given project path."""
        logger.info(f"Loading dbt project metadata for project located at {project_path}")
        # Must have otherwise adapter is not getting registered
        dbtRunner().invoke(["-q", "debug"], project_dir=str(project_path))
        # profile = load_profile(str(project_path), {})
        # project = load_project(str(project_path), version_check=False, profile=profile)
        # project_path = project_path
        # logger.info(f"Loaded project {project.project_name} with profile details:\n{mf_pformat(profile)}")
        return cls(profile=None, project=None, project_path=None)

    @property
    def dbt_paths(self) -> dbtPaths:
        """Return the bundle of configuration paths."""
        return dbtPaths(
            model_paths=self.project.model_paths,
            seed_paths=self.project.seed_paths,
            target_path=self.project.target_path,
        )

    @property
    def schema(self) -> str:
        """Return the adapter schema."""
        return self.profile.credentials.schema


@dataclasses.dataclass
class dbtArtifacts:
    """Container with access to the dbt artifacts required to power the MetricFlow CLI.

    In order to avoid double-loading this should generally be built from the dbtProjectMetadata struct.
    This does not inherit because it is a slightly different struct. In most cases this is the object
    we want to reference.
    """

    profile: Profile
    project: Project
    adapter: BaseAdapter
    semantic_manifest: SemanticManifest

    @classmethod
    def load_from_project_metadata(cls: Type[Self], project_metadata=None, adapter=None, semantic_json_path=None) -> Self:
        """Loads adapter and semantic manifest associated with the previously-fetched project metadata."""
        # dbt's get_adapter helper expects an AdapterRequiredConfig, but `project` is missing cli_vars
        # In practice, get_adapter only actually requires HasCredentials, so we replicate the type extraction
        # from get_adapter here rather than spinning up a full RuntimeConfig instance
        # TODO: Move to a fully supported interface when one becomes available
        from argparse import Namespace
        from dbt.flags import set_flags
        set_flags(Namespace(USE_COLORS=True, MACRO_DEBUGGING=False, PROFILES_DIR="/Users/jdhiman/.dbt"))
        adapter = get_adapter_by_type(load_profile("/Users/jdhiman/projects/inmetrics-prototype/in-dbt-examples/in-dbt-examples/src/metrics_example", {}).credentials.type)
        # semantic_manifest = dbtArtifacts.build_semantic_manifest_from_path(semantic_json_path)
        semantic_manifest = dbtArtifacts.build_semantic_manifest_from_path(semantic_json_path)
        return cls(
            profile=load_profile("/Users/jdhiman/projects/inmetrics-prototype/in-dbt-examples/in-dbt-examples/src/metrics_example", {}),
            project=None,
            adapter=adapter,
            semantic_manifest=semantic_manifest,
        )

    @classmethod
    def load_from_api_metadata(cls: Type[Self], adapter, semantic_json) -> Self:
        """Loads adapter and semantic manifest associated with the previously-fetched project metadata."""
        # dbt's get_adapter helper expects an AdapterRequiredConfig, but `project` is missing cli_vars
        # In practice, get_adapter only actually requires HasCredentials, so we replicate the type extraction
        # from get_adapter here rather than spinning up a full RuntimeConfig instance
        # TODO: Move to a fully supported interface when one becomes available
        # print(load_profile(str("~/.dbt/profiles.yml"), {}).credentials.type)
        from argparse import Namespace
        from dbt.flags import set_flags
        # TODO: JD - Temporary handling for Namespace issue
        set_flags(Namespace(USE_COLORS=True, MACRO_DEBUGGING=False, PROFILES_DIR="/Users/jdhiman/.dbt"))
        adapter = get_adapter_by_type(adapter)
        semantic_manifest = parse_manifest_from_dbt_generated_manifest(semantic_json)

        # TODO: JD - Temporary handling for profiles
        return cls(
            profile=load_profile("/Users/jdhiman/projects/inmetrics-prototype/in-dbt-examples/in-dbt-examples/src/metrics_example", {}),
            project=None,
            adapter=adapter,
            semantic_manifest=semantic_manifest,
        )

    @staticmethod
    def build_semantic_manifest_from_dbt_project_root(project_root: Path) -> SemanticManifest:
        """In the dbt project root, retrieve the manifest path and parse the SemanticManifest."""
        DEFAULT_TARGET_PATH = "target/semantic_manifest.json" # Input to the API
        full_path_to_manifest = Path(project_root, DEFAULT_TARGET_PATH).resolve()
        if not full_path_to_manifest.exists():
            raise ModelCreationException(
                f"Unable to find {full_path_to_manifest}\n"
                "Please ensure that you are running `mf` in the root directory of a dbt project "
                "and that the semantic_manifest JSON exists. If this is your first time running "
                "`mf`, run `dbt parse` to generate the semantic_manifest JSON."
            )
        try:
            with open(full_path_to_manifest, "r") as file:
                raw_contents = file.read()
                return parse_manifest_from_dbt_generated_manifest(manifest_json_string=raw_contents)
        except Exception as e:
            raise ModelCreationException from e

    @staticmethod
    def build_semantic_manifest_from_path(semantic_path: Path) -> SemanticManifest:
        full_path_to_manifest = Path(semantic_path).resolve()
        with open(semantic_path, "r") as file:
            raw_contents = file.read()
            return parse_manifest_from_dbt_generated_manifest(manifest_json_string=raw_contents)

