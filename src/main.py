
from transaction_reader import TransactionReader
from transaction_repository import TransactionRepository


def run(source_path, db_path):
    reader = TransactionReader(source_path).read_transactions()
    repository = TransactionRepository(db_path)    

    repository.create_table()
    repository.save(reader)
    repository.close()


run("data/transacoes.csv", "transactions.db")   