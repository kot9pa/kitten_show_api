from typing import TYPE_CHECKING, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.models import Base
if TYPE_CHECKING:    
    from src.api_v1.breeds.models import Breed


class Kitten(Base):
    name: Mapped[str]
    age: Mapped[int]
    color: Mapped[str]
    description: Mapped[str]
    
    breed_id: Mapped[int] = mapped_column(ForeignKey("breeds.id"))
    breed: Mapped["Breed"] = relationship(back_populates="kittens", 
                                          cascade="save-update, merge")
    
    def to_dict(self):
        return {
            "id": self.id,
            "breed_id": self.breed_id,
            "name": self.name,
            "age": self.age,
            "color": self.color,
            "description": self.description,
        }
