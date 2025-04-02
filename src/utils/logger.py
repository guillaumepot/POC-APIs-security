#src/utils/logger.py

from fastapi import FastAPI, Request, HTTPException
import logging
import logging.config
import os
from starlette.middleware.base import BaseHTTPMiddleware
import urllib.parse

from src.config.config import LOGGER_CONFIG

class LoggerManager:
    @staticmethod
    def configure_logger(name:str =' default', logger_config:dict = LOGGER_CONFIG, verbose: bool = False) -> logging.Logger:

        if name not in logger_config["logging"]["loggers"]:
            raise ValueError(f"Logger {name} not found in logging config file")
        else:
            log_directory = os.path.dirname(logger_config["logging"]["handlers"]["file"]["filename"])
            os.makedirs(log_directory, exist_ok=True)
            logging.config.dictConfig(logger_config["logging"])

            logger = logging.getLogger(name)

            if verbose:
                level = logging.DEBUG
            else:
                level = logging.INFO
            
            logger.setLevel(level)

            return logger
        


class ApiLogger(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.logger = LoggerManager.configure_logger(name='app', verbose=True)


    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        headers = request.headers
        user_agent = headers.get("User-Agent", "unknown")
        authorization = headers.get("Authorization", "unknown")

        if authorization != "unknown":
            authorization = "REDACTED"

        body = await request.body()
        body_str = body.decode("utf-8")
        sanitized_body_str = self.sanitize_body(body_str)

        if sanitized_body_str == '':
            self.logger.info(f"Request: {request.method} {request.url}")
            self.logger.info (f"from {client_ip}")
            self.logger.info(f"Headers: User-Agent={user_agent}, Authorization={authorization}")
        else:
            self.logger.info(f"Request: {request.method} {request.url}")
            self.logger.info (f"from {client_ip}")
            self.logger.info(f"Headers: User-Agent={user_agent}, Authorization={authorization}")
            self.logger.info(f"Body: {sanitized_body_str}")

        
        try:
            response = await call_next(request)
        except HTTPException as e:
            self.logger.error(f"Exception raised in {request.method} {request.url}: {e.detail}")
            raise e
        

        self.logger.info(f"Response status: {response.status_code}\n")
        return response


    def sanitize_body(self, body_str: str) -> str:
        parsed_body = urllib.parse.parse_qs(body_str)

        if "password" in parsed_body:
            parsed_body["password"] = ["masked_from_logs"]

        sanitized_body_str = urllib.parse.urlencode(parsed_body, doseq=True)
        return sanitized_body_str