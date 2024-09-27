"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from kedro_pypi_to_snowflake.pipelines.etl import pipeline as etl_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["etl"] = etl_pipeline.create_pipeline()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
