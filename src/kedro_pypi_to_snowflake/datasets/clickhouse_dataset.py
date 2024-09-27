import clickhouse_connect
from kedro.io import AbstractDataset
import pyarrow as pa

class ClickHouseDataset(AbstractDataset[pa.Table, pa.Table]):
    def __init__(self, sql: str, host: str, username: str, database: str, secure: bool = True, port: int = 443):
        """Initialize the dataset with SQL query and connection details for ClickHouse."""
        self.sql = sql
        self.host = host
        self.username = username
        self.database = database
        self.secure = secure
        self.port = port

    def _load(self) -> pa.Table:
        """Query ClickHouse and return an Arrow Table."""
        client = clickhouse_connect.get_client(
            host=self.host,
            username=self.username,
            database=self.database,
            secure=self.secure,
            port=self.port,
        )
        # Return Arrow result from ClickHouse
        return client.query_arrow(self.sql)

    def _save(self, data: pa.Table) -> None:
        """Not implemented for this dataset as it's for reading only."""
        raise NotImplementedError("Save is not implemented for this dataset")

    def _describe(self) -> dict:
        """Provide a description of the dataset."""
        return {
            "sql": self.sql,
            "host": self.host,
            "username": self.username,
            "database": self.database,
            "secure": self.secure,
            "port": self.port,
        }