
from pydantic import BaseModel

class FinanceCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: str
    notes: str
