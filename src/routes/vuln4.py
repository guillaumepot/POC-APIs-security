# src/routes/vuln4.py
# Unrestricted Resource Consumption

# Lib
from fastapi import APIRouter, Request
from src.utils.rate_limiter import rate_limiter


"""
Router Declaration
"""
vulnerability4 = APIRouter()


"""
Routes Declaration
"""
@vulnerability4.get("/vuln4/broken/limited_route", tags=["Vuln IV"])
def broken_limited_route():
    return {'info': 'API is running'}


@vulnerability4.get("/vuln4/fixed/limited_route", tags=["Vuln IV"])
@rate_limiter.limit("5/minute")
def fixed_limited_route(request: Request):
    return {'info': 'API is running'}