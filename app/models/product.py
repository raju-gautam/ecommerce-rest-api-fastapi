from app.database import Base
from sqlalchemy import Column,Integer,Float,String,Text

class Product(Base):
    __tablename__ = "products"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    price=Column(Float,nullable=False)
    description=Column(Text,nullable=False)
    stock=Column(Integer,default=0)
    category=Column(String(50),nullable=True)







