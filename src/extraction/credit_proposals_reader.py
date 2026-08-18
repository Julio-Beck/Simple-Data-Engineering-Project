from src.domain.models import CreditProposal
from src.extraction.base_reader import BaseReader

class CreditProposalReader(BaseReader[CreditProposal]):
    def query(self) -> str:
        return "SELECT * FROM propostas_credito;"

    def map_row(self, row:dict) -> CreditProposal:
        return CreditProposal(
            id=row["cod_proposta"],
            customer_id=row["cod_cliente"],
            collaborator_id=row["cod_colaborador"],
            proposal_submitted_at=row["data_entrada_proposta"],
            monthly_interest_rate=row["taxa_juros_mensal"],
            proposal_amount=row["valor_proposta"],
            financing_amount=row["valor_financiamento"],
            down_payment=row["valor_entrada"],
            installment_amount=row["valor_prestacao"],
            installment_count=row["quantidade_parcelas"],
            grace_period=row["carencia"],
            status=row["status_proposta"]
        )




reader = CreditProposalReader("localhost", 55432, "banvic", "data_engineer", 123456)
credit_proposals = reader.read()

for pro in credit_proposals:
    print(pro)
    print(" ")