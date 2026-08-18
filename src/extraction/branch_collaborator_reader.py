from src.domain.models import BranchCollaborator
from src.extraction.base_reader import BaseReader


class BranchCollaboratorReader(BaseReader[BranchCollaborator]):
    def query(self) -> str:
        return "SELECT * FROM colaborador_agencia;"

    def map_row(self, row:dict) -> BranchCollaborator:
        return BranchCollaborator(
            collaborator_id=row["cod_colaborador"],
            branch_id=row["cod_agencia"]
        )



reader = BranchCollaboratorReader("localhost", 55432, "banvic", "data_engineer", 123456)

branchcol = reader.read()
for bc in branchcol:
    print(bc)
    print(" ")