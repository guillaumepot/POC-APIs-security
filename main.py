#main.py

# Lib
import uvicorn
from src.config.config import API_HOST, API_PORT


"""
Start uvicorn server
"""
if __name__ == '__main__':
    uvicorn.run("src.app:app",
                host = API_HOST,
                port = API_PORT,
                reload = True)