#src/utils/security_functions.py


# Lib
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt

from config.config import SECRET_KEY, ALGORITHM, JWT_EXPIRE


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")



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