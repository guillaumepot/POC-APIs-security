# src/routes/vuln7.py
# Server Side Request Forgery

# Lib
from fastapi import APIRouter
from src.utils.host_command_execution import run_vulnerable_shell_command


"""
Router Declaration
"""
vulnerability7 = APIRouter()


"""
Routes Declaration
"""
@vulnerability7.get("/vuln7/broken/shell_command", tags=["Vuln VII"])
def broken_shell_command(command: str = 'hostname'):
    result = run_vulnerable_shell_command(command = command)
    return {'info': result}