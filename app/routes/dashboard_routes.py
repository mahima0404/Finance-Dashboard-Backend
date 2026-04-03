
from fastapi import APIRouter

router = APIRouter()

@router.get("/summary")
def get_summary():
    return {
        "total_income": 50000,
        "total_expense": 20000,
        "net_balance": 30000
    }
