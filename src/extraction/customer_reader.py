from src.extraction.base_reader import BaseReader
from src.domain.models import Customer, CustomerType

class CustomerReader(BaseReader[Customer]):
    def query(self) -> str:
        return "SELECT * FROM clientes;"


    def map_row(self, row: dict) -> Customer:
        return Customer(
            id=row["cod_cliente"],
            first_name=row["primeiro_nome"],
            last_name=row["ultimo_nome"],
            email=row["email"],
            type=CustomerType(row["tipo_cliente"]),
            inclusion_date=row["data_inclusao"],
            cpf_cnpj=row["cpfcnpj"],
            birth_date=row["data_nascimento"],
            address=row["endereco"],
            zip_code=row["cep"]
        )



#reader = CustomerReader("localhost", 55432, "banvic", "data_engineer", 123456)
#branches = reader.read()
#for branch in branches:
#    print(branch)
#    print(" ")