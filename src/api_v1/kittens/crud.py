from sqlalchemy import select, delete
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from src.api_v1.breeds.models import Breed
from src.api_v1.kittens.models import Kitten
from src.api_v1.kittens.schemas import KittenCreate, KittenUpdate, KittenUpdatePartial


async def get_kittens(session: AsyncSession) -> list | None:
    stmt = select(Kitten).options(joinedload(Kitten.breed)).order_by(Kitten.id)
    results = await session.scalars(stmt)
    kittens = results.all()
    if not kittens:
        return {"message": "Kittens not found"}
    kittens_to_return = []
    for kitten in kittens:
        kitten_data = kitten.to_dict()
        kitten_data['breed'] = kitten.breed.title
        kittens_to_return.append(kitten_data)
    return kittens_to_return

async def get_kitten(session: AsyncSession, kitten_id: int) -> dict | None:
    stmt = select(Kitten).options(joinedload(Kitten.breed)).filter_by(id=kitten_id)
    kitten = await session.scalar(stmt)
    if not kitten:
        return {"message": f"Kitten by id={kitten_id} not found"}
    kitten_data = kitten.to_dict()
    kitten_data['breed'] = kitten.breed.title
    return kitten_data

async def get_kitten_by_id(session: AsyncSession, kitten_id: int) -> Kitten | None:
    stmt = select(Kitten).where(Kitten.id == kitten_id)
    return await session.scalar(stmt)

async def get_kittens_by_breed(session: AsyncSession, breed: Breed) -> list[Kitten]:
    stmt = select(Kitten).options(joinedload(Kitten.breed)).filter_by(breed_id=breed.id)
    results = await session.scalars(stmt)
    kittens = results.all()
    if not kittens:
        return {"message": f"Kitten by breed_id={breed.id} not found"}
    kittens_to_return = []
    for kitten in kittens:
        kitten_data = kitten.to_dict()        
        kitten_data['breed'] = kitten.breed.title
        kittens_to_return.append(kitten_data)
    return kittens_to_return

async def create_kitten(session: AsyncSession, kitten_in: KittenCreate) -> Kitten:
    kitten = Kitten(**kitten_in.model_dump(exclude_none=True))
    session.add(kitten)
    try:
        await session.commit()
        return kitten
    except SQLAlchemyError as err:
        await session.rollback()
        raise err

async def update_kitten(session: AsyncSession, 
                      kitten: Kitten, kitten_update: KittenUpdate | KittenUpdatePartial,
                      partial: bool = False) -> Kitten:
    for key, value in kitten_update.model_dump(exclude_unset=partial).items():
        setattr(kitten, key, value)
    try:
        await session.commit()
        return kitten
    except SQLAlchemyError as err:
        await session.rollback()
        raise err

async def delete_kitten(session: AsyncSession, kitten: Kitten = None):
    await session.delete(kitten)
    try:
        await session.commit()
        return {"message": f"Kitten by id={kitten.id} deleted successfully"}
    except SQLAlchemyError as err:
        await session.rollback()
        raise err
    
async def delete_kittens(session: AsyncSession):
    await session.execute(delete(Kitten))
    try:
        await session.commit()
        return {"message": "All kittens deleted successfully"}
    except SQLAlchemyError as err:
        await session.rollback()
        raise err