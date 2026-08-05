from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    transaction_id: int
    account_number: int
    transaction_date: datetime 
    transaction_type: str
    amount: float



