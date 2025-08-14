from app.api.v1.endpoints.book import router as book_router
from app.api.v1.endpoints.auth import router as auth_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(book_router)
router.include_router(auth_router)

