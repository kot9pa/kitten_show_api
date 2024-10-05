from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.breeds import crud
from src.api_v1.breeds.schemas import Breed, BreedView
from src.dependencies import breed_by_id
from src.database import db_helper


router = APIRouter(prefix="/breeds", tags=["Breed"])

@router.get("/", response_model=list[BreedView])
async def get_breeds(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_breeds(session=session)

@router.get("/{id}/", summary="Get Breed By Id", response_model=BreedView)
async def get_breed(
    breed: Breed = Depends(breed_by_id),
):
    return breed
