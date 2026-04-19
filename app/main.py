from fastapi import FastAPI   
from app.database import Base, engine
from app.models import User,Product,Cart,Order
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.routes import auth
from app.routes import products
from app.routes import cart
from app.routes import order

app = FastAPI()

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(order.router)


# Create Tables
Base.metadata.create_all(bind=engine)



# Test API 

@app.get("/")

def home():
    return {"message": "Hello Raju Welcome to E-Commerce API"}







               