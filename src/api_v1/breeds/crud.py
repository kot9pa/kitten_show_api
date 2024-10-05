from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.breeds.models import Breed


async def get_breeds(session: AsyncSession) -> list[Breed]:
    stmt = select(Breed)
    result = await session.scalars(stmt)
    return list(result)

async def get_breed_by_id(session: AsyncSession, breed_id: int) -> Breed | None:
    stmt = select(Breed).where(Breed.id == breed_id)
    return await session.scalar(stmt)
