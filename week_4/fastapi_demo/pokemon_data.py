from typing import Optional

from pydantic import BaseModel


class Pokemon(BaseModel):
    name: str
    type: str
    level: float


class UpdatePokemon(BaseModel):
    name: str | None = None
    type: Optional[str] = None
    level: Optional[float] = None
