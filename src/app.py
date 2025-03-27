#src/app.py

# Lib
from fastapi import FastAPI

from src.config.config import api_tags
from src.routes.vuln1 import vulnerability1
from src.routes.login import authenticator


"""
API Declaration
"""
app = FastAPI(
    title = "OWASP Top 10 APIs - 2023",
    description = "APIs with unsecure routes and mitigations to show OWASP TOP 10 APIs (2023).",
    version = "1.0.0",
    openapi_tags = api_tags,
    debug = True
    )


"""
OWASP vuln routers
"""
app.include_router(vulnerability1, tags=["Vuln I"])
app.include_router(authenticator, tags=["Utils"])