import psycopg2 
from psycopg2.extras import RealDictCursor
# from typing import List, Dict

class PostgresConnection:
    def __init__(self, host, port, database, user, password):
        self.connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def execute_query(self, query: str, params = tuple()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()