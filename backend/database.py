import os
import sqlite3
from pathlib import Path

INSTANCE_DIR = Path(__file__).parent / 'instance'
DB_PATH = os.environ.get('DATABASE_PATH', str(INSTANCE_DIR / 'database.db'))


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    INSTANCE_DIR.mkdir(exist_ok=True)
    conn = get_connection()
    try:
        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            )
            '''
        )
        conn.commit()
    finally:
        conn.close()
