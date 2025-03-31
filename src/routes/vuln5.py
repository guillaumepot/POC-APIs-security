# src/routes/vuln5.py
# 

# Lib
from fastapi import APIRouter, Request
from src.utils.rate_limiter import rate_limiter


"""
Router Declaration
"""
vulnerability5 = APIRouter()


"""
Routes Declaration
"""
@vulnerability5.get("/vuln4/broken/limited_route", tags=["Vuln IV"])
def broken_limited_route():
    return {'info': 'API is running'}


@vulnerability5.get("/vuln4/fixed/limited_route", tags=["Vuln IV"])
@rate_limiter.limit("5/minute")
def fixed_limited_route(request: Request):
    return {'info': 'API is running'}