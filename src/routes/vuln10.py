# src/routes/vuln10.py
#  Unsafe Consumption of APIs


# Lib
from fastapi import APIRouter, HTTPException
import sqlite3

from src.config.config import DB_NAME
from src.utils.sqlite_engine import SqliteEngine


"""
Router Declaration
"""
vulnerability10 = APIRouter()


"""
Routes Declaration
"""
# SQL injeciton examples:
    # ' OR 1=1;--
    # ' UNION SELECT username, password FROM users --'
@vulnerability10.get("/vuln10/broken/sql_query", tags=["Vuln X"])
def broken_user_info(username: str):
    try:
        conn = sqlite3.connect(DB_NAME, check_same_thread = False)
        cursor = conn.cursor()
        cursor.execute(f"SELECT firstname, lastname FROM users WHERE username = '{username}'")
        response = cursor.fetchall()
    except sqlite3.Error as e:
        raise e
    else:
        if not response:
            raise HTTPException(status_code=404, detail="Username not found")
        else:
            return response
    finally:
        conn.close()


@vulnerability10.get("/vuln10/fixed/sql_query", tags=["Vuln X"])
def fixed_user_info(username: str):
    try:
        conn = sqlite3.connect(DB_NAME, check_same_thread = False)
        cursor = conn.cursor()
        cursor.execute("SELECT firstname, lastname FROM users WHERE username = ?", (username,))
        response = cursor.fetchall()
    except sqlite3.Error as e:
        raise e
    else:
        if not response:
            raise HTTPException(status_code=404, detail="Username not found")
        else:
            return response
    finally:
        conn.close()