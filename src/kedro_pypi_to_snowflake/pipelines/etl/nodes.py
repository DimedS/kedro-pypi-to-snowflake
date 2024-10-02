"""
This is a boilerplate pipeline 'etl'
generated using Kedro 0.19.8
"""
import pandas as pd
import pyarrow as pa

def convert_arrow_to_snowpark(data: pa.Table):
    df = data.to_pandas()
    df['date'] = pd.to_datetime(df['date'], unit='D', origin='1970-01-01').dt.date
    df.columns = df.columns.str.upper()
    return df