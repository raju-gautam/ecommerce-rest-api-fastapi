from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# import os
# from dotenv import load_dotenv
# load_dotenv()

# DATABASE URL
# DATABASE_URL= os.getenv("DATABASE_URL")



# DATABASE URL
DATABASE_URL="mysql+pymysql://root:Raju%40123@localhost:3306/ecommerce_db"

# create engine
engine = create_engine(DATABASE_URL)

# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create base
Base = declarative_base()



# Test DATABASE connection
try:
    db=engine.connect()
    print("DATABASE connect sucess")
except:
    print("DATABASE not connect")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

