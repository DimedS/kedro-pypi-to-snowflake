"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import convert_arrow_to_snowpark


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=convert_arrow_to_snowpark,
                inputs="clickhouse_pypi_downloads",
                outputs="snowflake_pypi_downloads",  # Pandas will be converted to Snowpark inside of .safe()
                name="convert_arrow_to_snowpark_node",
            ),
        ]
    )
