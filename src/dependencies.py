from typing import Annotated
from fastapi import HTTPException, Path, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.kittens import crud as crud_kitten
from src.api_v1.kittens.schemas import Kitten
from src.api_v1.breeds import crud as breed_kitten
from src.api_v1.breeds.schemas import Breed
from src.database import db_helper


async def kitten_by_id(
    id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Kitten:
    result = await crud_kitten.get_kitten_by_id(session=session, kitten_id=id)
    if result is not None:
        return result
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Kitten not found",
    )

async def breed_by_id(
    id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Breed:
    result = await breed_kitten.get_breed_by_id(session=session, breed_id=id)
    if result is not None:
        return result
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Breed not found",
    )
