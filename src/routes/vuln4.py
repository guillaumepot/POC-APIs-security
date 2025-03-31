# src/routes/vuln4.py
# Unrestricted Resource Consumption

# Lib
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse

from src.config.config import CAPTCHA_SITE_KEY, HTML_TEMPLATES_DIR
from src.utils.rate_limiter import rate_limiter
from src.utils.captcha import verify_captcha





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


@vulnerability4.get("/vuln4/fixed/captcha", response_class=HTMLResponse, tags=["Vuln IV"])
def serve_captcha_page(request: Request):
    site_key = CAPTCHA_SITE_KEY
    return HTML_TEMPLATES_DIR.TemplateResponse("captcha_form.html", {"request": request, "site_key": site_key})


@vulnerability4.post("/vuln4/fixed/captcha_route", tags=["Vuln IV"])
def capcha_limited_route(request: Request, captcha_token: str = Form(...)):
    remote_ip = request.client.host
    if not verify_captcha(captcha_token, remote_ip):
        raise HTTPException(status_code=400, detail="Invalid CAPTCHA")
    
    return HTML_TEMPLATES_DIR.TemplateResponse("solved_captcha.html", {"request": request})
