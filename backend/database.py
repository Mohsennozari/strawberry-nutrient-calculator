import os
import sqlite3
from pathlib import Path

# ============================================================
# تنظیمات دیتابیس
# ============================================================
INSTANCE_DIR = Path(__file__).parent / 'instance'
DB_PATH = os.environ.get('DATABASE_PATH', str(INSTANCE_DIR / 'database.db'))


def get_connection():
    """دریافت اتصال به دیتابیس"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """ایجاد جدول‌های مورد نیاز"""
    INSTANCE_DIR.mkdir(exist_ok=True)
    conn = get_connection()
    try:
        # جدول کاربران
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

        # جدول تاریخچه محاسبات (برای نسخه بعدی)
        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS calculations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                stage TEXT NOT NULL,
                ppm TEXT NOT NULL,
                health_status TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            )
            '''
        )

        conn.commit()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"❌ Database error: {e}")
        raise
    finally:
        conn.close()
