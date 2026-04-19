# E-Commerce Backend REST API (FastAPI)

E-commerce backend API built using FastAPI.
This project provides APIs for users, products, cart, and orders with authentication.

## 🚀 Features

* User registration & login (JWT Authentication)
* Role based access (Admin / User)
* Product CRUD (Create, Read, Update, Delete)
* Cart management
* Order management
* MySQL database integration
* Clean project structure
* Environment variables support


## 📁 Project Structure

ecommerce_api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── cart.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── product_schema.py
│   │   ├── order_schema.py
│   │   └── cart_schema.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── products.py
│   │   ├── cart.py
│   │   └── orders.py
│   │
│   ├── core/
│   │   ├── security.py
│   │   └── config.py
│   │
│   └── utils/
│       └── dependencies.py
│
├── requirements.txt
├── .env
└── README.md


## ⚙️ Installation

### 1. Clone repository

git https://github.com/raju-gautam/ecommerce-rest-api-fastapi.git
cd ecommerce_api

### 2. Create virtual environment

python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Linux / Mac:

source venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Setup Environment Variables (.env)

Create `.env` file:

DATABASE_URL=mysql+pymysql://user:password@localhost:3306/ecommerce_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60


## ▶️ Run Server

uvicorn app.main:app --reload

Server will start at:

http://127.0.0.1:8000


## 📚 API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc


## 🔐 Authentication

This project uses JWT token authentication.

1. Register user
2. Login user
3. Get access token
4. Use token in headers:

Authorization: Bearer your_token


## 🧪 Main APIs

### Auth

* Register User
* Login User

### Users

* Get Profile
* Get All Users (Admin)

### Products

* Create Product (Admin)
* Get Products
* Update Product (Admin)
* Delete Product (Admin)

### Cart

* Add to cart
* View cart
* Remove item

### Orders

* Create order
* Get user orders
* Get all orders (Admin)


## 🛠 Tech Stack

* FastAPI
* Python
* MySQL
* SQLAlchemy
* Pydantic
* JWT Authentication
* Uvicorn


## 👨‍💻 Author

Raju Gautam
Backend Developer – Python | FastAPI | MySQL


## 📄 License

This project is for learning purpose.

  
  
