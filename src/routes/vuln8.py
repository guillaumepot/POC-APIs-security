# src/routes/vuln8.py
# Security Misconfiguration

# Lib
from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse

from src.config.config import LOGS_FILEPATH
from src.utils.security_functions import sanitize_logs, get_current_user, require_role


"""
Router Declaration
"""
vulnerability8 = APIRouter()


"""
Routes Declaration
"""
@vulnerability8.get("/vuln8/broken/logs", tags=["Vuln VIII"], response_class=PlainTextResponse)
def broken_logs():
    with open(LOGS_FILEPATH, 'r') as file:
        logs = file.read()
    return logs


@vulnerability8.get("/vuln8/fixed/logs", tags=["Vuln VIII"])
@require_role(roles=[9])
def fixed_logs(current_user: dict = Depends(get_current_user)):
    with open(LOGS_FILEPATH, 'r') as file:
        logs = file.readlines()

    sanitized_logs = sanitize_logs(logs)

    return sanitized_logs