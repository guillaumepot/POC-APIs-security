# src/routes/vuln3.py
# Broken Object Property Level Authorization

# Lib
from fastapi import APIRouter, Depends, HTTPException

from src.config.config import DB_NAME
from src.config.data_models import BrokenUserModel, FixeduserModel
from src.utils.security_functions import get_current_user
from src.utils.sqlite_engine import SqliteEngine


"""
Router Declaration
"""
vulnerability3 = APIRouter()


"""
Routes Declaration
"""
@vulnerability3.get("/vuln3/broken/activity", tags=["Vuln III"])
def get_user_activity_vuln(activity: str, current_user: dict = Depends(get_current_user)):
    # Query
    query = """
            SELECT DISTINCT *
            FROM activity a
            JOIN users u
            ON a.user_id = u.id
            WHERE a.activity = ?;
            """

    # DB request
    try:
        SqliteEngine(DB_NAME).connect()
        response = SqliteEngine(DB_NAME).select(query, (activity,))
    finally:
        SqliteEngine(DB_NAME).close()

    # Return
    if not response:
        raise HTTPException(status_code=404, detail="No logs found")

    return response


@vulnerability3.get("/vuln3/fixed/activity", tags=["Vuln III"])
def get_user_activity_fix(activity: str, current_user: dict = Depends(get_current_user)):
    # Query
    query = """
            SELECT DISTINCT u.username, a.activity, a.date, a.device
            FROM activity a
            JOIN users u
            ON a.user_id = u.id
            WHERE a.activity = ?;
            """

    # DB request
    try:
        SqliteEngine(DB_NAME).connect()
        response = SqliteEngine(DB_NAME).select(query, (activity,))
    finally:
        SqliteEngine(DB_NAME).close()

    # Return
    if not response:
        raise HTTPException(status_code=404, detail="No logs found")

    return response


@vulnerability3.post("/vuln3/broken/register", tags=["Vuln III"])
def broken_register(user_data:BrokenUserModel) -> dict:

    # try:
    #     SqliteEngine(DB_NAME).connect()
    #     SqliteEngine(DB_NAME).insert("users")
    # except ValueError:
    #     raise HTTPException(status_code=500, detail="Database error")
    # else:
    #     return {"info": f"Successfully registred {user_data.username}"}
    # finally:
    #     SqliteEngine(DB_NAME).close()


@vulnerability3.post("/vuln3/fixed/register", tags=["Vuln III"])
def fixed_register():
    pass


# - Créer la route /register broken (permet de forcer le role à admin)
# - Créer la route /register fixed (empêche la modification de role)