from typing import Annotated, List
from fastapi import APIRouter, Path, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.kittens import crud
from src.api_v1.kittens.schemas import Kitten, KittenView, KittenCreate, KittenUpdate, KittenUpdatePartial
from src.api_v1.breeds.schemas import Breed
from src.dependencies import kitten_by_id, breed_by_id
from src.database import db_helper


router = APIRouter(prefix="/kittens", tags=["Kitten"])

@router.get("/", response_model_exclude_none=List[KittenView])
async def get_kittens(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_kittens(session=session)

@router.get("/{id}/", summary="Get Kitten By Id", response_model_exclude_none=KittenView)
async def get_kitten(
    id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_kitten(session=session, kitten_id=id)

@router.get("/by_breed/{id}/", response_model_exclude_none=List[KittenView])
async def get_kittens_by_breed(
    breed: Breed = Depends(breed_by_id), 
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_kittens_by_breed(session=session, breed=breed)

@router.post("/", response_model=Kitten, status_code=status.HTTP_201_CREATED)
async def create_kitten(
    kitten_in: KittenCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_kitten(session=session, kitten_in=kitten_in)

@router.put("/{id}/")
async def update_kitten(
    kitten_update: KittenUpdate,
    kitten: Kitten = Depends(kitten_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_kitten(
        session=session,
        kitten=kitten,
        kitten_update=kitten_update,
    )

@router.patch("/{id}/", summary="Partial Update Kitten")
async def update_kitten(
    kitten_update: KittenUpdatePartial,
    kitten: Kitten = Depends(kitten_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_kitten(
        session=session,
        kitten=kitten,
        kitten_update=kitten_update,
        partial=True,
    )

@router.delete("/", summary="Delete All Kittens")
async def delete_kittens(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.delete_kittens(session=session)

@router.delete("/{id}/")
async def delete_kitten(
    kitten: Kitten = Depends(kitten_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.delete_kitten(session=session, kitten=kitten)
