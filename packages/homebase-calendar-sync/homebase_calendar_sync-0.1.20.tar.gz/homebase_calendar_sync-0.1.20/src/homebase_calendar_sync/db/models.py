import sqlite3
from pathlib import Path
from .. import config


def connect_database():
    config.DB = sqlite3.connect(config.DB_NAME)
    config.DB_CURSOR = config.DB.cursor()


def setup_database():
    config.DB = sqlite3.connect(config.DB_NAME)
    config.DB_CURSOR = config.DB.cursor()
    config.DB_CURSOR.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id TEXT NOT NULL UNIQUE,
            hash TEXT NOT NULL,
            from_homebase INTEGER NOT NULL CHECK (from_homebase IN (0, 1)),
            homebase_shift_id TEXT UNIQUE
        )
    """
    )
    config.DB_CURSOR.execute(
        """
        CREATE TABLE IF NOT EXISTS shifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            homebase_shift_id TEXT NOT NULL UNIQUE,
            hash TEXT NOT NULL
        )
    """
    )
    config.DB.commit()


def reset_database():
    db_path = Path.cwd() / config.DB_NAME
    try:
        db_path.unlink()
    except FileNotFoundError:
        print("no events database to reset")
