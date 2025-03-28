# src/routes/vuln3.py
# Broken Object Property Level Authorization

# Lib
from fastapi import APIRouter, Depends, HTTPException

from src.config.config import DB_NAME
from src.utils.security_functions import get_current_user
from src.utils.sqlite_engine import SqliteEngine

"""
Router Declaration
"""
vulnerability3 = APIRouter()


"""
Routes Declaration
"""
@vulnerability3.get("/vuln3/broken/activity/{id: int}", tags=["Vuln III"])
def get_user_activity_vuln(activity: str): #, current_user: dict = Depends(get_current_user)
    # Query
    query = """
            SELECT DISTINCT *
            FROM activity a
            JOIN collaborators c
            ON a.user_id = c.id
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


@vulnerability3.get("/vuln3/fixed/activity/{id: int}", tags=["Vuln III"])
def get_user_activity_fix(id: int, activity: str): #, current_user: dict = Depends(get_current_user)
    pass






# - Créer la route retournant des info sur l'activité mais avec moins d'info

# - Créer la route /register broken (permet de forcer le role à admin)
# - Créer la route /register fixed (empêche la modification de role)