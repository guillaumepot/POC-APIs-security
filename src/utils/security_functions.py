#src/utils/security_functions.py


# Lib
from collections import Counter
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from functools import wraps
import jwt
import re

from src.config.config import SECRET_KEY, ALGORITHM, JWT_EXPIRE

# Var
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")



# Functions
def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception as e:
        print(f"An error occurred while decoding the token: {e}")
    
    return payload


def encode_jwt(payload_to_encode: dict) -> str:
    token_expiration = timedelta(minutes = JWT_EXPIRE)
    expire = datetime.now() + token_expiration 
    payload_to_encode["exp"] = expire

    # Encode
    encoded_jwt = jwt.encode(payload = payload_to_encode,
                             key = SECRET_KEY,
                             algorithm=ALGORITHM,
                             headers = None,
                             json_encoder = None)

    return encoded_jwt




def sanitize_logs(logs:str):
    status_codes = Counter()
    error_details = []

    status_code_pattern = re.compile(r"Response status: (\d{3})")
    request_pattern = re.compile(r"Request: (GET|POST|PUT|DELETE) (http[^\s]+)")
    from_pattern = re.compile(r"from ([\d\.]+)")
    headers_pattern = re.compile(r"Headers: (.+)")
    body_pattern = re.compile(r"body:\s*(.*)")


    request_url = None
    request_from = None
    request_headers = None
    request_body = None


    for line in logs:
        if request_pattern.search(line):
            request_url = request_pattern.search(line).group(2)
        if from_pattern.search(line):
            request_from = from_pattern.search(line).group(1)
        if headers_pattern.search(line):
            request_headers = headers_pattern.search(line).group(1)
        if body_pattern.search(line):
            request_body = body_pattern.search(line).group(1)
        
        status_match = status_code_pattern.search(line)


        if status_match:
            status_code = status_match.group(1)
            status_codes[status_code] += 1
            
            if status_code != "200":
                error_details.append({
                    "status_code": status_code,
                    "url": request_url,
                    "from": request_from,
                    "headers": request_headers,
                    "body": request_body
                })


    return JSONResponse(content={
        "status_codes": dict(status_codes),
        "errors": error_details
    })




# Decorators
def require_role(roles: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_data = kwargs.get("current_user")
            if not user_data or user_data.get("role") not in roles:
                raise HTTPException(status_code=401, detail="Not authorized")
            return func(*args, **kwargs)
        return wrapper
    return decorator