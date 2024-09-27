"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import convert_arrow_to_snowpark


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=convert_arrow_to_snowpark,
                inputs=["kedro_all_total_downloads"],  # Input datasets (PyArrow + Snowflake session)
                outputs="snowflake_data",  # Output Snowpark DataFrame
                name="convert_arrow_to_snowpark_node",
            ),
        ]
    )
