# src/routes/vuln6.py
# Unrestricted Access to Sensitive Business Flows

# Lib
from fastapi import APIRouter, Depends, Request

from src.utils.rate_limiter import rate_limiter
from src.utils.security_functions import get_current_user, require_role

"""
Router Declaration
"""
vulnerability6 = APIRouter()


"""
Routes Declaration
"""
@vulnerability6.get("/vuln6/broken/unrestricted_route", tags=["Vuln VI"])
def broken_unrestricted_route():
    return {'info': 'Your request has been processed !'}

@vulnerability6.get("/vuln6/fixed/unrestricted_route", tags=["Vuln VI"])
@rate_limiter.limit("1/second")
@require_role(roles=[2,9])
def fixed_unrestricted_route(request: Request, current_user: dict = Depends(get_current_user)):
    print(f"Current user: {current_user}")
    return {'info': f'Your request has been processed ! Authorized roles: 2 & 9. you role: {current_user['role']}'}
