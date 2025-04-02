# src/routes/vuln7.py
# Server Side Request Forgery


# to fully exploit the broken route:
    # - Start a python http-server on your host or another server
    # - Put files to test the broken route
    # - To go further: Try to execute a reverse shell

# Lib
from fastapi import APIRouter, HTTPException
import requests
from urllib.parse import urlparse

from src.config.config import ALLOWED_DOMAINS

"""
Router Declaration
"""
vulnerability7 = APIRouter()


"""
Routes Declaration
"""
@vulnerability7.get("/vuln7/broken/fetch", tags=["Vuln VII"])
def broken_fetch_url(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="Missing URL")

    try:
        response = requests.get(url)
        exec(response.text)
        return {"status": response.status_code, "content": response.text[:200]}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))



@vulnerability7.get("/vuln7/fixed/fetch", tags=["Vuln VII"])
def fixed_fetch_url(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="Missing URL")
    
    parsed_url = urlparse(url)
    domain = parsed_url.hostname
    
    if parsed_url.scheme not in ("http", "https"):
        raise HTTPException(status_code=400, detail="Invalid URL scheme")
    
    if domain not in ALLOWED_DOMAINS:
        raise HTTPException(status_code=403, detail="Domain not allowed")
    
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        return {"status": response.status_code, "content": response.text[:200]}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))









