from pydantic import BaseModel

class OrderResponse(BaseModel):
    id: int
    total_price: float
    status: str

    class Config:
        from_attributes = True