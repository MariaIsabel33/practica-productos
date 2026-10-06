from typing import Literal
from pydantic import BaseModel, Field

class ProductoIn(BaseModel):
    nombre: str = Field(min_length=1, max_length=100)
    sku: str = Field(min_length=1, max_length=30)
    precio: float = Field(ge=0)
    stock: int = Field(default=0, ge=0)
    categoria: Literal["ropa", "tecnologia", "hogar"]