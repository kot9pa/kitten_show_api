from pydantic import BaseModel, ConfigDict, Field


class KittenBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    breed_id: int
    name: str
    age: int = Field(ge=1, le=12)
    color: str
    description: str

class Kitten(KittenBase):
    id: int

class KittenView(Kitten):
    breed: str

class KittenCreate(KittenBase):
    pass

class KittenUpdate(KittenCreate):
    pass

class KittenUpdatePartial(KittenCreate):
    breed_id: int | None = None
    age: int = Field(ge=1, le=12, default=None)
    name: str | None = None
    color: str | None = None
    description: str | None = None    
