from src.domain.models import Account, CustomerType
from src.extraction.base_reader import BaseReader

class AccountReader(BaseReader[Account]):
    def query(self) -> str:
        return "SELECT * FROM contas"

    def map_row(self, row:dict) -> Account:
        return Account(
            number=row["num_conta"],
            customer_id=row["cod_cliente"],
            branch_id=row["cod_agencia"],
            collaborator_id=row["cod_colaborador"],
            type=CustomerType(row["tipo_conta"]),
            opening_date=row["data_abertura"],
            total_balance=row["saldo_total"],
            available_balance=row["saldo_disponivel"],
            last_transaction_at=row["data_ultimo_lancamento"]
        )



#reader = AccountReader("localhost", 55432, "banvic", "data_engineer", 123456)
#accounts = reader.read()
#for ac in accounts:
#    print(ac)
#    print(" ")

