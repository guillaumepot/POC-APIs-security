# src/routes/vuln9.py
# Improper Inventory Management

# Lib
from fastapi import APIRouter, Depends, HTTPException

from src.config.config import DB_NAME
from src.utils.security_functions import get_current_user, require_role
from src.utils.sqlite_engine import SqliteEngine


"""
Router Declaration
"""
vulnerability9 = APIRouter()


"""
Routes Declaration
"""
@vulnerability9.get("/vuln9/beta/user_info", tags=["Vuln IX"])
def broken_user_info(username: str):
    # Query
    query = "SELECT * FROM users WHERE username = ?"

    # DB request
    try:
        SqliteEngine(DB_NAME).connect()
        response = SqliteEngine(DB_NAME).select(query, (username,))
    finally:
        SqliteEngine(DB_NAME).close()

    # Return
    if not response:
        raise HTTPException(status_code=404, detail="Collaborator not found")
    else:
        return response
    

@vulnerability9.get("/vuln9/administration/user_info", tags=["Vuln IX"])
@require_role(roles=[9])
def fixed_user_info(username: str, current_user: dict = Depends(get_current_user)):
    # Query
    query = "SELECT * FROM users WHERE username = ?"

    # DB request
    try:
        SqliteEngine(DB_NAME).connect()
        response = SqliteEngine(DB_NAME).select(query, (username,))
    finally:
        SqliteEngine(DB_NAME).close()

    # Return
    if not response:
        raise HTTPException(status_code=404, detail="Collaborator not found")
    else:
        return response