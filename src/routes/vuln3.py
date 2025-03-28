# src/routes/vuln3.py
# Broken Object Property Level Authorization

# Lib
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException

from src.config.config import DB_NAME
from src.config.data_models import BrokenUserModel, FixedUserModel
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
def broken_register(user_data: BrokenUserModel) -> dict:
    values_to_insert = user_data.to_db_values()
    # return {'info': values_to_insert}

    try:
        SqliteEngine(DB_NAME).connect()
        last_id = SqliteEngine(DB_NAME).select("SELECT id FROM users ORDER BY id DESC LIMIT 1")
        id = int(last_id[0][0]) + 1
        values_to_insert.insert(0, id)
        SqliteEngine(DB_NAME).insert("users", values_to_insert)
    except ValueError:
        raise HTTPException(status_code=500, detail="Database error")
    else:
        return {"info": f"Successfully registred {values_to_insert[3]}"}
    finally:
        SqliteEngine(DB_NAME).close()



@vulnerability3.post("/vuln3/fixed/register", tags=["Vuln III"])
def fixed_register(user_data: FixedUserModel):
    values_to_insert = user_data.to_db_values()

    try:
        SqliteEngine(DB_NAME).connect()
        last_id = SqliteEngine(DB_NAME).select("SELECT id FROM users ORDER BY id DESC LIMIT 1")
        id = int(last_id[0][0]) + 1
        values_to_insert.insert(0, id)
        SqliteEngine(DB_NAME).insert("users", values_to_insert)
    except ValueError:
        raise HTTPException(status_code=500, detail="Database error")
    else:
        return {"info": f"Successfully registred {values_to_insert[3]}"}
    finally:
        SqliteEngine(DB_NAME).close()