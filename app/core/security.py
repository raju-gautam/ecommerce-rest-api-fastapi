from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext


# Secret key & Algorithm
SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 180


# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Fake current user (for testing)
def get_current_user():
    return {"id": 1, "username": "testuser"}


# Hash password
def hash_password(password: str):
    return pwd_context.hash(password)



# Verify password
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# Create Access Token
def create_access_token(data: dict, expires_delta: timedelta = None):

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


# Verify JWT Token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None



