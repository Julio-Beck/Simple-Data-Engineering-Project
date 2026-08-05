import csv
from transaction import Transaction
from datetime import datetime

class TransactionReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_transactions(self) -> list[Transaction]:
        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            transactions = []
            for row in reader:
                transactions.append(
                    Transaction(
                        transaction_id= int(row["cod_transacao"]),
                        account_number = int(row["num_conta"]),
                        transaction_date = datetime.fromisoformat(row["data_transacao"].replace(" UTC", "")),
                        transaction_type = str(row["nome_transacao"]),
                        amount = float(row["valor_transacao"])
                    )
                )

            return transactions

