#src/config/config.py

from dotenv import load_dotenv
import json
import os
import yaml

from src.utils.cryptography import generate_secret_key


# Config loaders
load_dotenv(dotenv_path='./src/config/.env',
            override = False)



# CONST
DB_NAME = os.getenv("DB_NAME")
API_HOST = os.getenv("API_HOST")
API_PORT = int(os.getenv("API_PORT"))

with open("./src/config/logger_config.yaml", "r") as f:
    LOGGER_CONFIG = yaml.safe_load(f)


with open("./src/config/example_database_tables.yaml", "r") as f:
    DB_PRECONFIG = yaml.safe_load(f)
    EXAMPLE_TABLES = DB_PRECONFIG['tables']

with open("./src/config/example_database_data.json", "r") as f:
    EXAMPLE_DATA = json.load(f)


# LOGIN Config
SECRET_KEY = generate_secret_key()
ALGORITHM = "HS256"
JWT_EXPIRE = 30




# Api Tags
api_tags = [
    {
        'name': 'Utils',
        'description': 'Utilities'
    },
    {
        'name': 'Vuln I',
        'description': 'Broken Object Level Authorisation (BOLA)'
    },
    {
        'name': 'Vuln II',
        'description': 'Broken User Authentication (BUA)'
    },
    {
        'name': 'Vuln III',
        'description': 'Broken Object Property Level Authorization'
    },
    {
        'name': 'Vuln IV',
        'description': 'Unrestricted Resource Consumption'
    },
    {
        'name': 'Vuln V',
        'description': 'Broken Function Level Authorisation'
    },
    {
        'name': 'Vuln VI',
        'description': 'Unrestricted Access to Sensitive Business Flows'
    },
    {
        'name': 'Vuln VII',
        'description': 'Server Side Request Forgery'
    },
    {
        'name': 'Vuln VIII',
        'description': 'Security Misconfiguration'
    },
    {
        'name': 'Vuln IX',
        'description': 'Improper Inventory Management'
    },
    {
        'name': 'Vuln X',
        'description': 'Unsafe Consumption of APIs'
    },
]