from pydantic import BaseModel, ConfigDict


class BreedBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str

class Breed(BreedBase):
    id: int

class BreedView(Breed):
    pass

class BreedCreate(BreedBase):
    pass

class BreedUpdate(BreedCreate):
    pass

class BreedUpdatePartial(BreedCreate):
    title: str | None = None