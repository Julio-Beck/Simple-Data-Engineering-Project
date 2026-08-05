import sqlite3 
from transaction import Transaction
class TransactionRepository:

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY,
            account_number INTEGER NOT NULL,
            transaction_date TEXT NOT NULL,
            transaction_type TEXT NOT NULL,
            amount REAL NOT NULL
        );
        """
        self.cursor.execute(query)
    
    def save(self, transactions: list[Transaction]):
        data = ((
            transaction.transaction_id,
            transaction.account_number,
            transaction.transaction_date.isoformat(),
            transaction.transaction_type,
            transaction.amount
            )
            for transaction in transactions

            )
        
        self.cursor.executemany(
            """
            INSERT OR IGNORE INTO transactions (
                transaction_id,
                account_number,
                transaction_date,
                transaction_type,
                amount
            )
            VALUES (?, ?, ?, ?, ?);
            """,
            data
        )

        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

