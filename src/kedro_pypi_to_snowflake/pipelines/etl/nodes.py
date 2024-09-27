"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.19.8
"""
import pyarrow as pa
import snowflake.snowpark as sp

def convert_arrow_to_snowpark(data: pa.Table) -> sp.DataFrame:

    return data.to_pandas()