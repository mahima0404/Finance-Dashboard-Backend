
from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_user(user: dict):
    return {"msg": "User created", "user": user}

@router.get("/")
def get_users():
    return {"users": []}
