import os
import sqlite3
from pathlib import Path

# ============================================================
# تنظیمات دیتابیس
# ============================================================
INSTANCE_DIR = Path(__file__).parent / 'instance'
DB_PATH = os.environ.get('DATABASE_PATH', str(INSTANCE_DIR / 'database.db'))


def get_connection():
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

        # ✅ جدول تاریخچه محاسبات با ستون‌های کامل
        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS calculations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                stage TEXT NOT NULL,
                ppm TEXT NOT NULL,
                ratios TEXT NOT NULL,
                health_status TEXT NOT NULL,
                fruit_weight REAL,
                alerts TEXT,
                recommendations TEXT,
                input_data TEXT NOT NULL,
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


# ============================================================
# توابع کمکی
# ============================================================

def save_calculation(user_id, result, input_data):
    """ذخیره محاسبه در دیتابیس"""
    import json

    conn = get_connection()
    try:
        conn.execute(
            '''
            INSERT INTO calculations (
                user_id, stage, ppm, ratios, health_status,
                fruit_weight, alerts, recommendations, input_data
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                user_id,
                result.get('stage', ''),
                json.dumps(result.get('ppm', {})),
                json.dumps(result.get('ratios', {})),
                result.get('health_status', ''),
                result.get('fruit_weight_prediction', 0),
                json.dumps(result.get('alerts', {})),
                json.dumps(result.get('recommendations', [])),
                json.dumps(input_data)
            )
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error saving calculation: {e}")
        return False
    finally:
        conn.close()


def get_user_calculations(user_id, limit=10):
    """دریافت تاریخچه محاسبات کاربر"""
    conn = get_connection()
    try:
        import json
        rows = conn.execute(
            '''
            SELECT * FROM calculations
            WHERE user_id = ?
            ORDER BY created_at DESC
            LIMIT ?
            ''',
            (user_id, limit)
        ).fetchall()

        calculations = []
        for row in rows:
            calculations.append({
                'id': row['id'],
                'stage': row['stage'],
                'ppm': json.loads(row['ppm']),
                'ratios': json.loads(row['ratios']),
                'health_status': row['health_status'],
                'fruit_weight': row['fruit_weight'],
                'alerts': json.loads(row['alerts']) if row['alerts'] else {},
                'recommendations': json.loads(row['recommendations']) if row['recommendations'] else [],
                'created_at': row['created_at']
            })
        return calculations
    except Exception as e:
        print(f"❌ Error getting calculations: {e}")
        return []
    finally:
        conn.close()


def get_calculation_stats(user_id):
    """دریافت آمار محاسبات کاربر"""
    conn = get_connection()
    try:
        total = conn.execute(
            'SELECT COUNT(*) as count FROM calculations WHERE user_id = ?',
            (user_id,)
        ).fetchone()

        last = conn.execute(
            'SELECT created_at, health_status, stage FROM calculations WHERE user_id = ? ORDER BY created_at DESC LIMIT 1',
            (user_id,)
        ).fetchone()

        return {
            'total': total['count'] if total else 0,
            'last_calculation': last['created_at'] if last else None,
            'last_health_status': last['health_status'] if last else None,
            'last_stage': last['stage'] if last else None
        }
    except Exception as e:
        print(f"❌ Error getting stats: {e}")
        return {'total': 0, 'last_calculation': None, 'last_health_status': None, 'last_stage': None}
    finally:
        conn.close()
