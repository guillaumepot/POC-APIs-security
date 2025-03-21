#src/scripts/generate_example_database.py

from config.config import DB_NAME, EXAMPLE_TABLES, EXAMPLE_DATA
from modules.logger import LoggerManager
from modules.sqlite_engine import SqliteEngine


logger = LoggerManager.configure_logger(name='script', verbose=False)



if __name__ == '__main__':
    logger.info("Starting database generation script")

    SqliteEngine(DB_NAME).connect()

    # Generate tables
    for table in EXAMPLE_TABLES:
        SqliteEngine(DB_NAME).create_table(table)

    SqliteEngine(DB_NAME).show_tables()

    # Insert data
    for data in EXAMPLE_DATA:
        SqliteEngine(DB_NAME).insert(data['table'], data['values'])

    SqliteEngine(DB_NAME).close()

    logger.info("Database generation script completed")