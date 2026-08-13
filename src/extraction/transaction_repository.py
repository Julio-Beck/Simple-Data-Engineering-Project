import sqlite3 
from src.domain.models   import Transaction
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

    def count_transaction(self):
        query = """
           SELECT COUNT(*)
           FROM transactions
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def total_amount_by_type(self):
        query = """
            SELECT transaction_type, SUM(amount) AS total
            FROM transactions
            GROUP BY transaction_type
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def monthly_transaction_volume(self):
        query = """
            SELECT strftime('%Y-%m', transaction_date) AS month, SUM(amount) AS transaction_count
            FROM transactions
            GROUP BY month
            ORDER BY month;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

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

