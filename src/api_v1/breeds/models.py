from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, relationship

from src.models import Base
if TYPE_CHECKING:    
    from src.api_v1.kittens.models import Kitten

class Breed(Base):
    title: Mapped[str]

    kittens: Mapped[list["Kitten"]] = relationship(back_populates="breed")
