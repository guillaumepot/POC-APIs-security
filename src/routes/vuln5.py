# src/routes/vuln5.py
# Broken Function Level Authorization

# Lib
from fastapi import APIRouter, Depends

from src.utils.security_functions import get_current_user, require_role

"""
Router Declaration
"""
vulnerability5 = APIRouter()


"""
Routes Declaration
"""
@vulnerability5.get("/vuln5/broken/limited_to_admin", tags=["Vuln V"])
def broken_limited_to_admin_route(current_user: dict = Depends(get_current_user)):
    return {'info': f'Welcome {current_user['sub']}, Your role is: {current_user['role']}. This route is broken !'}


@vulnerability5.get("/vuln5/fixed/limited_to_admin", tags=["Vuln V"])
@require_role(role = 9)
def fixed_limited_to_admin_route(current_user: dict = Depends(get_current_user)):
    return {'info': f'Welcome {current_user['sub']}, Your role is: {current_user['role']}. Route fixed !'}
