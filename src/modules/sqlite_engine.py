#src/modules/sqlite_engine.py

from modules.logger import LoggerManager
import sqlite3


class SqliteEngine():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SqliteEngine, cls).__new__(cls)
        return cls._instance


    def __init__(self, DB_NAME):
        if not hasattr(self, 'initialized'):
            self.DB_NAME = DB_NAME
            self._initialized = True
            self.logger = LoggerManager.configure_logger(name='SQLiteEngine', verbose=True)


    def connect(self):
        try:
            self.conn = sqlite3.connect(self.DB_NAME)
            self.cursor = self.conn.cursor()
            self.logger.info(f"Connected to {self.DB_NAME}")
        except sqlite3.Error as e:
            self.logger.error(f"Error connecting to {self.DB_NAME}: {e}")
            raise e


    def close(self):
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
            self.logger.info(f"Closed connection to {self.DB_NAME}")
        else:
            self.logger.warning(f"Attempted to close a connection that was never established to {self.DB_NAME}")


    def create_table(self, table:dict):
        table_name = table['name']
        columns = table['columns']
        columns_with_types = ", ".join(f"{col['name']} {col['type']}" for col in columns)

        try:
            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})')
            self.logger.info(f"Table {table_name} created with columns: {', '.join(col['name'] for col in columns)}")
        except ValueError as ve:
            self.logger.error(f"Error creating table {table_name}: {ve}")
            raise ve
        except sqlite3.Error as e:
            self.logger.error(f"Error creating table {table_name}: {e}")
            raise e
            

    def show_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        self.logger.info(f"Current tables in database: {self.cursor.fetchall()}")
    

    def insert(self, table_name:str, values:list):
        placeholders = ', '.join(['?'] * len(values))
        try:
            self.cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', values)
            self.conn.commit()
            self.logger.info(f"Inserted values into {table_name}: {values}")
        except sqlite3.Error as e:
            self.logger.error(f"Error inserting values into {table_name}: {e}")
            raise e

    def select(self, query):
        try:
            self.cursor.execute(query)
        except sqlite3.Error as e:
            self.logger.error(f"Error executing query {query}: {e}")
            raise e
        else:
            self.logger.info(f"{self.cursor.fetchall()}")

