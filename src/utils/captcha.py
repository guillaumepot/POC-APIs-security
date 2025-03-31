#src/utils/captcha.py


# Lib
import requests

from src.config.config import CAPTCHA_VERIFY_URL, CAPTCHA_SECRET





def verify_captcha(token: str, remote_ip: str) -> bool:
    response = requests.post(
        CAPTCHA_VERIFY_URL,
        data={
            "secret": CAPTCHA_SECRET,
            "response": token,
            "remoteip": remote_ip
        }
    )
    result = response.json()
    return result.get("success", False)