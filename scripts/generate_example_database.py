#scripts/generate_example_database.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from datetime import datetime, timedelta
import random

from src.config.config import DB_NAME, EXAMPLE_TABLES, EXAMPLE_DATA
from src.utils.hashing import hash_string
from src.utils.logger import LoggerManager
from src.utils.sqlite_engine import SqliteEngine


logger = LoggerManager.configure_logger(name='script', verbose=False)


def gen_random_activity(nb_entries = 100):
    user_ids = [2,3,4,5,6]
    activities = ['log in', 'log out', 'read_mail', 'send_mail', 'incoming_phone_call', 'open_app', 'close_app', 'download_file']
    user_devices = {
        2: ['laptop_1001', 'android_2001'],
        3: ['laptop_1002', 'ios_3001'],
        4: ['desktop_4001', 'android_2002'],
        5: ['desktop_4002', 'android_2003'],
        6: ['desktop_4003', 'ios_3002'],
    }
    date_start = datetime(2025, 3, 25)


    generated_activities = []
    for i in range(1, nb_entries + 1):
        user_id = random.choice(user_ids)
        activity = random.choice(activities)
        date = date_start + timedelta(days=random.randint(0, 10), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        device = random.choice(user_devices[user_id])
        
        entry = {
            "id": i,
            "user_id": user_id,
            "activity": activity,
            "date": date.strftime('%Y-%m-%d %H:%M:%S'),
            "device": device
        }
        generated_activities.append(entry)

    return generated_activities


if __name__ == '__main__':
    logger.info("Starting database generation script")

    # Remove existing database.db:
    os.remove(DB_NAME) if os.path.exists(DB_NAME) else None

    # Generate random activity data
    generated_activities = gen_random_activity(nb_entries = 300)


    # --- Generate tables and insert data --- #
    SqliteEngine(DB_NAME).connect()

    # Drop if exists | Generate tables
    for table in EXAMPLE_TABLES:
        SqliteEngine(DB_NAME).create_table(table)

    SqliteEngine(DB_NAME).show_tables()

    # Insert user & role data
    for data in EXAMPLE_DATA['roles']:
        SqliteEngine(DB_NAME).insert('roles', list(data.values()))
    for data in EXAMPLE_DATA['users']:
        # Hash password
        data['password'] = hash_string(data['password'])
        SqliteEngine(DB_NAME).insert('users', list(data.values()))
    # Insert activity generated data
    for row in generated_activities:
        SqliteEngine(DB_NAME).insert('activity', list(row.values()))


    SqliteEngine(DB_NAME).close()

    logger.info("Database generation script completed")