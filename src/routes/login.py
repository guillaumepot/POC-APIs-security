#src/routes/login.py


# Lib
from fastapi import APIRouter, HTTPException

# from config.config import DB_NAME
from utils.cryptography import generate_secret_key
# from utils.sqlite_engine import SqliteEngine


# db_engine = SqliteEngine(DB_NAME)
secret_key = generate_secret_key()


"""
Router Declaration
"""
authenticator = APIRouter()



