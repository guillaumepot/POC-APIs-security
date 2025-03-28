# src/routes/vuln2.py
# Broken Authentication

# Lib
from fastapi import APIRouter, HTTPException

from src.config.config import DB_NAME
from src.utils.security_functions import encode_jwt
from src.utils.sqlite_engine import SqliteEngine

"""
Router Declaration
"""
vulnerability2 = APIRouter()


"""
Routes Declaration
"""


@vulnerability2.post("/vuln2/broken/login", tags=["Vuln II"])
def broken_login(username: str, password: str):
    # Get users
    query = "SELECT id, name, role from users WHERE name = ?"
    try:
        SqliteEngine(DB_NAME).connect()
        response = SqliteEngine(DB_NAME).select(query, (username,))
    finally:
        SqliteEngine(DB_NAME).close()

    # Check if user exists
    if not response:
        raise HTTPException(status_code=404, detail="Invalid username")

    else:
        user_data = {
            "id": response[0][0],
            "sub": response[0][1],
            "role": response[0][2],
        }
        token = encode_jwt(user_data)

        return {"access_token": token}


@vulnerability2.post("/vuln2/fixed/login", tags=["Vuln II"])
def fixed_login(username: str, password: str):
    return {"info": "Check the /login route which fix this vulnerability !"}