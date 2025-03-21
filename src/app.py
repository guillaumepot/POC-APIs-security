# api/main.py

# Lib
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded


import time
import uvicorn


from config.config import api_tags



"""
API Declaration
"""
app = FastAPI(
    title = "OWASP Top 10 APIs - 2023",
    description = "APIs with unsecure routes and mitigations to show OWASP TOP 10 APIs (2023).",
    version = 1,
    openapi_tags = api_tags,
    debug = True
    )
















#from routers.authenticator import authenticator
from utils.config import DEBUG, LOGGER, HOST, PORT, CURRENT_VERSION
from utils.exceptions import CustomException
from utils.limiter import limiter
from utils.logger import SanitizeLoggingMiddleware





"""
Logger Declaration
- Logger is disabled (default), to enable it: Set logger to True in .env file
"""


# Enable middleware if LOGGER is set to True
if LOGGER == "True":
    app.add_middleware(SanitizeLoggingMiddleware)



"""
Limiter Declaration
- Limiter is used to limit the number of requests per IP on the routes
"""
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, lambda request, exc: JSONResponse(
    status_code=429,
    content={"detail": f"Rate limit exceeded on this route. Rate: {exc.detail}"}
))

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    return response




"""
Exception Handler
- Custom exception handler used to return custom error messages.
- Custom exceptions are raised in the routers depending the route | name, error_code, message should be defined in the exception
"""

# Exception Handler
@app.exception_handler(CustomException)
def CustomExceptionHandler(request: Request, exception: CustomException):
    return JSONResponse(status_code=exception.error_code,
                        content={
                            'url': str(request.url),
                            'name': exception.name,
                            'message': exception.message,
                            'date': exception.date})



"""
Routers
"""
# app.include_router(authenticator)
# app.include_router(information)
# app.include_router(tester)



"""
Start uvicorn server
"""
if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
    last_run = time.time()