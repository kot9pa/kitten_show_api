from fastapi import APIRouter
from src.api_v1.kittens.views import router as kitten_router
from src.api_v1.breeds.views import router as breed_router

internal_router = APIRouter()
internal_router.include_router(router=kitten_router)
internal_router.include_router(router=breed_router)