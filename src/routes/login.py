#src/routes/login.py


# Lib
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.config.config import DB_NAME
from src.utils.hashing import verify_hash
from src.utils.security_functions import encode_jwt, get_current_user
from src.utils.sqlite_engine import SqliteEngine



"""
Router Declaration
"""
authenticator = APIRouter()


@authenticator.post('/login', tags=["Utils"])
def login(credentials: OAuth2PasswordRequestForm = Depends()):

    # Get users
    query = "SELECT id, name, password, role from users WHERE name = ?"
    try:
        SqliteEngine(DB_NAME).connect()
        response = SqliteEngine(DB_NAME).select(query, (credentials.username,))
    finally:
        SqliteEngine(DB_NAME).close()

    # Check if user exists
    if not response or not verify_hash(to_verify = credentials.password, hashed_value = response[0][2]):
        raise HTTPException(status_code = 404,
                            detail = "Invalid username or password")
    

    else:
        user_data = {
            'id' : response[0][0],
            'sub' : credentials.username,
            'role': response[0][3]
        }
        token = encode_jwt(user_data)

        return {"access_token": token}
    

@authenticator.get('/read_payload', tags=["Utils"])
def read_payload(payload: dict = Depends(get_current_user)):
    return payload