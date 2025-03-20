#src/config.py

from dotenv import load_dotenv
import os
import yaml

# Config loaders
load_dotenv(dotenv_path='./config/.env',
            override = False)



# CONST
DB_NAME = os.getenv("DB_NAME")

with open("./config/logger_config.yaml", "r") as f:
    LOGGER_CONFIG = yaml.safe_load(f)

with open("./config/example_database_data.yaml", "r") as f:
    EXAMPLE_TABLES = yaml.safe_load(f)['tables']
    EXAMPLE_DATA = yaml.safe_load(f)['data']