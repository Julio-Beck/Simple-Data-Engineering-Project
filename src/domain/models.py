from dataclasses import dataclass
from datetime import datetime
from datetime import date
from enum import Enum
from decimal import Decimal

@dataclass
class Transaction:
    transaction_id: int
    account_number: int
    transaction_date: datetime 
    transaction_type: str
    amount: float



class BranchType(Enum):
    DIGITAL = "Digital"
    PHYSICAL = "Física"

@dataclass
class Branch:
    id: int
    name: str
    address: str | None
    city: str | None
    state: str | None
    opening_date: date | None
    type: BranchType | None



class CustomerType(Enum):
    PF = "PF"
    PJ = "PJ"

@dataclass
class Customer:
    id: int
    first_name: str
    last_name: str
    email: str
    type: CustomerType | None
    inclusion_date: datetime | None
    cpf_cnpj: str 
    birth_date: date | None
    address: str | None
    zip_code: str | None



@dataclass 
class BranchCollaborator:
    collaborator_id: int
    branch_id: int

@dataclass
class Collaborator: 
    id: int
    first_name: str
    last_name: str
    email: str
    cpf: str
    birth_date: date | None
    address: str | None
    zip_code: str | None


@dataclass
class Account:
    number: int
    customer_id: int | None
    branch_id: int | None
    collaborator_id: int | None
    type: CustomerType | None
    opening_date: datetime | None
    total_balance: Decimal | None
    available_balance: Decimal | None
    last_transaction_at: datetime | None



class ProposalStatus(Enum):
    SUBMITTED = "Enviada"
    DOCUMENT_VALIDATION = "Validação documentos"
    APPROVED = "Aprovada"
    REJECTED = "Reprovada"
    UNDER_REVIEW = "Em análise"

@dataclass 
class CreditProposal:
    id: int
    customer_id: int | None
    collaborator_id: int | None
    proposal_submitted_at: datetime | None
    monthly_interest_rate: Decimal | None
    proposal_amount: Decimal | None
    financing_amount: Decimal | None
    down_payment: Decimal | None
    installment_amount: Decimal | None
    installment_count: int | None
    grace_period: int | None
    status: ProposalStatus | None






