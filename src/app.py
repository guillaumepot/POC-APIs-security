# src/app.py

# Lib
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

from src.config.config import api_tags
from src.routes.login import authenticator
from src.routes.vuln1 import vulnerability1
from src.routes.vuln2 import vulnerability2
from src.routes.vuln3 import vulnerability3
from src.routes.vuln4 import vulnerability4
from src.utils.rate_limiter import rate_limiter


"""
API Declaration
"""
app = FastAPI(
    title="OWASP Top 10 APIs - 2023",
    description="APIs with unsecure routes and mitigations to show OWASP TOP 10 APIs (2023).",
    version="1.0.0",
    openapi_tags=api_tags,
    debug=True,
)


@app.get("/", tags=["Utils"])
def hello() -> None:
    return {"info": "Go to swagger UI using /docs route"}



"""
OWASP vuln routers
"""
app.include_router(vulnerability1, tags=["Vuln I"])
app.include_router(vulnerability2, tags=["Vuln II"])
app.include_router(vulnerability3, tags=["Vuln III"])
app.include_router(vulnerability4, tags=["Vuln IV"])
app.include_router(authenticator, tags=["Utils"])


"""
Utils
"""
# Rate limiter (used for vuln IV)
app.state.limiter = rate_limiter
app.add_exception_handler(RateLimitExceeded, lambda request, exc: JSONResponse(
    status_code=429,
    content={"detail": f"Rate limit exceeded. Rate: {exc.detail}"}
))