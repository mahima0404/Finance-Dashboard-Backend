
from fastapi import APIRouter

router = APIRouter()

@router.post("/records")
def create_record(record: dict):
    return {"msg": "Record created", "record": record}

@router.get("/records")
def get_records():
    return {"records": []}
