#src/utils/security_functions.py


# Lib
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from functools import wraps
import ipaddress
import jwt
from urllib.parse import urlparse

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