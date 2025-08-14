from fastapi import APIRouter

router = APIRouter(prefix="/books")

@router.get("/")
def get_book():
    return {"Key":"Book found"}