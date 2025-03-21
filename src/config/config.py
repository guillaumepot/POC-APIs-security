#src/config/config.py

from dotenv import load_dotenv
import os
import yaml

# Config loaders
load_dotenv(dotenv_path='./config/.env',
            override = False)



# CONST
DB_NAME = os.getenv("DB_NAME")
API_HOST = os.getenv("API_HOST")
API_PORT = os.getenv("API_PORT")



with open("./config/logger_config.yaml", "r") as f:
    LOGGER_CONFIG = yaml.safe_load(f)

with open("./config/example_database_data.yaml", "r") as f:
    EXAMPLE_TABLES = yaml.safe_load(f)['tables']
    EXAMPLE_DATA = yaml.safe_load(f)['data']



# Api Tags

api_tags = [
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