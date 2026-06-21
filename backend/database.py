import os
import sqlite3
from pathlib import Path

INSTANCE_DIR = Path(__file__).parent / 'instance'
DB_PATH = os.environ.get('DATABASE_PATH', str(INSTANCE_DIR / 'database.db'))

CREATE_USERS_TABLE = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL COLLATE NOCASE,
        email TEXT UNIQUE NOT NULL COLLATE NOCASE,
        password_hash TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT (datetime('now'))
    )
'''


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _migrate_users_collation(conn):
    """Rebuild a legacy `users` table that lacks COLLATE NOCASE on username/email."""
    row = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='users'"
    ).fetchone()
    if row is None or 'COLLATE NOCASE' in row['sql'].upper():
        return

    conn.executescript(
        '''
        ALTER TABLE users RENAME TO users_legacy;
        ''' + CREATE_USERS_TABLE + ''';
        INSERT OR IGNORE INTO users (id, username, email, password_hash, created_at)
            SELECT id, username, email, password_hash, created_at FROM users_legacy;
        DROP TABLE users_legacy;
        '''
    )
    conn.commit()


def init_db():
    INSTANCE_DIR.mkdir(exist_ok=True)
    conn = get_connection()
    try:
        conn.execute(CREATE_USERS_TABLE)
        conn.commit()
        _migrate_users_collation(conn)
    finally:
        conn.close()
