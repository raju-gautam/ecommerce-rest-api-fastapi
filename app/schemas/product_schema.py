from pydantic import BaseModel
from typing import Optional

# ProductCreate Schema
class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    stock: int
    category: str

# ProductUpdate Schema
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    stock: Optional[int] = None
    category: Optional[str] = None

# ProductResponse Schema
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None
    stock: int
    category: str

    class Config:
        from_attributes = True 