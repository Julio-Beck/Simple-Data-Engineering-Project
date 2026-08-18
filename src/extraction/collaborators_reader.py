from src.domain.models import Collaborator
from src.extraction.base_reader import BaseReader

class CollaboratorReader(BaseReader[Collaborator]):
    def query(self) -> str:
        return "SELECT * FROM colaboradores";

    def map_row(self, row:dict) -> Collaborator:
        return Collaborator(
            id=row["cod_colaborador"],
            first_name=row["primeiro_nome"],
            last_name=row["ultimo_nome"],
            email=row["email"],
            cpf=row["cpf"],
            birth_date=row["data_nascimento"],
            address=row["endereco"],
            zip_code=row["cep"]
        )


#reader = CollaboratorReader("localhost", 55432, "banvic", "data_engineer", 123456)
#collaborators = reader.read()
#for collaborator in collaborators:
#    print(collaborator)
#    print(" ")