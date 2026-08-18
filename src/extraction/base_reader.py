from abc import ABC, abstractmethod
from src.extraction.postgres_connection import PostgresConnection
from typing import TypeVar, Generic


T = TypeVar("T")

class BaseReader(ABC, Generic[T]):
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def read(self) -> list[T]:
        with PostgresConnection(self.host, self.port, self.database, self.user, self.password) as connection:
            rows = connection.execute_query(self.query())
            return [self.map_row(row) for row in rows]

    @abstractmethod 
    def query(self) -> str:
        ...

    @abstractmethod
    def map_row(self, row: dict) -> T:
        ...