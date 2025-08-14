from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# from app.db.deps import get_db
from app.schemas import user

router = APIRouter(prefix="/auth")

@router.get("/")
def get_user():
    return {"key":"User found"}