"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.19.8
"""
import pyarrow as pa


def convert_arrow_to_snowpark(data: pa.Table):
    return data.to_pandas()
