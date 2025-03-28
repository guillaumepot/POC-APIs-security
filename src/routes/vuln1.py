# src/routes/vuln1.py
# Broken Object Level Authorization

# Lib
from fastapi import APIRouter, Depends, HTTPException

from src.config.config import DB_NAME
from src.utils.security_functions import get_current_user
from src.utils.sqlite_engine import SqliteEngine

# db_engine = SqliteEngine(DB_NAME)


"""
Router Declaration
"""
vulnerability1 = APIRouter()


"""
Routes Declaration
"""


@vulnerability1.get("/vuln1/broken/collaborator/{id:int}", tags=["Vuln I"])
def get_collaborator_info_vuln(id: int) -> dict:
    # Query
    query = "SELECT * FROM users WHERE id = ?"

    # DB request
    try:
        SqliteEngine(DB_NAME).connect()
        response = SqliteEngine(DB_NAME).select(query, (id,))
    finally:
        SqliteEngine(DB_NAME).close()

    # Return
    if not response:
        raise HTTPException(status_code=404, detail="Collaborator not found")

    else:
        collaborator_info = {
            "id": response[0][0],
            "firstname": response[0][1],
            "lastname": response[0][2],
            "username": response[0][3],
            "email": response[0][4],
            "phone": response[0][5],
            "department": response[0][6],
            "manager_id": response[0][7],       
            "annual_salary": response[0][8],
            "created_at": response[0][10],
            "role": response[0][11],
        }

        return collaborator_info

@vulnerability1.get("/vuln1/fixed/collaborator/{id:int}", tags=["Vuln I"])
def get_collaborator_info_secured(
    id: int, current_user: dict = Depends(get_current_user)
) -> dict:
    # Check if the user has authorization granted by role (here: is_admin == True)
    # Else, user can only check its own id
    is_admin = True if current_user["role"] == 9 else False
    if not is_admin and current_user["id"] != id:
        raise HTTPException(status_code=403, detail="Unauthorized access")

    # Query
    query = "SELECT * FROM users WHERE id = ?"

    # DB request
    try:
        SqliteEngine(DB_NAME).connect()
        response = SqliteEngine(DB_NAME).select(query, (id,))
    finally:
        SqliteEngine(DB_NAME).close()

    # Return
    if not response:
        raise HTTPException(status_code=404, detail="Collaborator not found")

    collaborator_info = {
        "id": response[0][0],
        "firstname": response[0][1],
        "lastname": response[0][2],
        "username": response[0][3],
        "email": response[0][4],
        "phone": response[0][5],
        "department": response[0][6],
        "manager_id": response[0][7],       
        "annual_salary": response[0][8],
        "created_at": response[0][10],
        "role": response[0][11],
    }

    return collaborator_info
