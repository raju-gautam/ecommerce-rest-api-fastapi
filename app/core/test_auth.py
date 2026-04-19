from security import hash_password, verify_password, create_access_token, verify_token

# Password test
password = "Raju123"

hashed = hash_password(password)
print("Hashed Password:", hashed)

# Verify password
check = verify_password("12345", hashed)
print("Password Match:", check)

# Create token
token = create_access_token({"sub": "raju@gmail.com"})
print("JWT Token:", token)

# Verify token
payload = verify_token(token)
print("Token Data:", payload)