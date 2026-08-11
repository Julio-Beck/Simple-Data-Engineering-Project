
from extraction.transaction_reader import TransactionReader
from extraction.transaction_repository import TransactionRepository


def run(source_path, db_path):
    reader = TransactionReader(source_path).read_transactions()
    repository = TransactionRepository(db_path)    
    repository.create_table()
    repository.save(reader)
    print(repository.total_amount_by_type())
    print(repository.monthly_transaction_volume())
    repository.close()


run("data/transacoes.csv", "transactions.db")   