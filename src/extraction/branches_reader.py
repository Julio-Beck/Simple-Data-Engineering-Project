from src.extraction.base_reader import BaseReader
from src.domain.models import Branch, BranchType


class BranchReader(BaseReader[Branch]):

    def query(self) -> str:
        return "SELECT * FROM agencias;"


    def map_row(self, row:dict) -> Branch:
        return Branch(
            id=row["cod_agencia"],
            name=row["nome"],
            address=row["endereco"],
            city=row["cidade"],
            state=row["uf"],
            opening_date=row["data_abertura"],
            type=BranchType(row["tipo_agencia"])
        )



#reader = BranchReader("localhost", 55432, "banvic", "data_engineer", 123456)
#branches = reader.read()
#for branch in branches:
#    print(branch)