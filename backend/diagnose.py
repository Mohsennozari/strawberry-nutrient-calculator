#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 تست کامل و عیب‌یابی سیستم
بدون نیاز به فرانت‌اند - فقط بک‌اند
"""

import json
import sqlite3
import sys
import requests
from pathlib import Path

BASE_URL = "http://127.0.0.1:5000"
TEST_USER = "diaguser"
TEST_PASS = "123456"

# ============================================================
# 1. بررسی دیتابیس
# ============================================================
def check_database():
    print("\n📁 1. بررسی دیتابیس:")
    db_path = Path(__file__).parent / "instance" / "database.db"

    if not db_path.exists():
        print("   ❌ فایل دیتابیس وجود ندارد!")
        return False

    print(f"   ✅ دیتابیس پیدا شد: {db_path}")

    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()

        # بررسی جدول users
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        if cursor.fetchone():
            print("   ✅ جدول users وجود دارد")
        else:
            print("   ❌ جدول users وجود ندارد!")
            return False

        # بررسی جدول calculations
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='calculations'")
        if cursor.fetchone():
            print("   ✅ جدول calculations وجود دارد")
        else:
            print("   ❌ جدول calculations وجود ندارد!")
            print("   ⚠️  باید جدول ساخته شود")
            return False

        # بررسی ستون‌های جدول calculations
        cursor.execute("PRAGMA table_info(calculations)")
        columns = [col[1] for col in cursor.fetchall()]
        required = ['user_id', 'stage', 'ppm', 'ratios', 'health_status', 'input_data']
        missing = [c for c in required if c not in columns]

        if missing:
            print(f"   ❌ ستون‌های کم‌دار: {missing}")
            return False
        else:
            print("   ✅ ساختار جدول calculations درست است")

        conn.close()
        return True

    except Exception as e:
        print(f"   ❌ خطای دیتابیس: {e}")
        return False


# ============================================================
# 2. بررسی سرور
# ============================================================
def check_server():
    print("\n🌐 2. بررسی سرور:")

    try:
        resp = requests.get(f"{BASE_URL}/health", timeout=3)
        if resp.status_code == 200:
            print(f"   ✅ سرور پاسخ می‌دهد (Status: {resp.status_code})")
            return True
        else:
            print(f"   ❌ سرور پاسخ غیرعادی: {resp.status_code}")
            return False
    except requests.ConnectionError:
        print("   ❌ سرور Flask روشن نیست!")
        print("   ▶  دستور: cd backend && python app.py")
        return False
    except Exception as e:
        print(f"   ❌ خطا: {e}")
        return False


# ============================================================
# 3. تست ثبت‌نام و ورود
# ============================================================
def test_auth():
    print("\n🔐 3. تست احراز هویت:")

    # حذف کاربر قبلی (از دیتابیس)
    db_path = Path(__file__).parent / "instance" / "database.db"
    if db_path.exists():
        try:
            conn = sqlite3.connect(str(db_path))
            conn.execute("DELETE FROM users WHERE username = ?", (TEST_USER,))
            conn.commit()
            conn.close()
        except:
            pass

    # ثبت‌نام
    try:
        resp = requests.post(
            f"{BASE_URL}/auth/register",
            json={"username": TEST_USER, "email": f"{TEST_USER}@test.com", "password": TEST_PASS},
            timeout=5
        )
        if resp.status_code == 201:
            print("   ✅ ثبت‌نام موفق")
        else:
            print(f"   ⚠️ ثبت‌نام: {resp.status_code}")
    except Exception as e:
        print(f"   ❌ خطا در ثبت‌نام: {e}")
        return None

    # ورود
    try:
        resp = requests.post(
            f"{BASE_URL}/auth/login",
            json={"username": TEST_USER, "password": TEST_PASS},
            timeout=5
        )
        if resp.status_code == 200:
            token = resp.json().get('token')
            print("   ✅ ورود موفق")
            print(f"   توکن: {token[:30]}...")
            return token
        else:
            print(f"   ❌ ورود ناموفق: {resp.status_code}")
            print(f"   پاسخ: {resp.text}")
            return None
    except Exception as e:
        print(f"   ❌ خطا در ورود: {e}")
        return None


# ============================================================
# 4. تست محاسبه
# ============================================================
def test_calculation(token):
    print("\n🧮 4. تست محاسبه:")

    if not token:
        print("   ❌ توکن وجود ندارد")
        return None

    data = {
        "crown_diameter": 15,
        "plant_height": 25,
        "petiole_length": 15,
        "leaf_length": 7,
        "leaf_width": 5.5,
        "fruit_size": 6,
        "age_days": 60,
        "fruits_per_plant": 6,
        "temp_c": 25,
        "weather": "sunny",
        "ec": 1.8,
        "ph": 6.0,
        "cultivar": "Albion"
    }

    headers = {"Authorization": f"Bearer {token}"}

    try:
        resp = requests.post(
            f"{BASE_URL}/calculate",
            json=data,
            headers=headers,
            timeout=10
        )

        if resp.status_code == 200:
            result = resp.json()
            print(f"   ✅ محاسبه موفق: مرحله {result.get('stage', 'نامشخص')}")
            return result
        else:
            print(f"   ❌ محاسبه ناموفق: {resp.status_code}")
            print(f"   پاسخ: {resp.text[:200]}")
            return None
    except Exception as e:
        print(f"   ❌ خطا در محاسبه: {e}")
        return None


# ============================================================
# 5. تست ذخیره (مهمترین قسمت)
# ============================================================
def test_save(token, result):
    print("\n💾 5. تست ذخیره محاسبه (مهم):")

    if not token:
        print("   ❌ توکن وجود ندارد")
        return False

    if not result:
        print("   ❌ نتیجه محاسبه وجود ندارد")
        return False

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "result": result,
        "input_data": {"crown_diameter": 15}
    }

    print("   📤 ارسال درخواست به: /calculations/save")

    try:
        resp = requests.post(
            f"{BASE_URL}/calculations/save",
            json=payload,
            headers=headers,
            timeout=10
        )

        print(f"   وضعیت: {resp.status_code}")

        if resp.status_code == 200:
            print("   ✅ ذخیره موفق!")
            print(f"   پاسخ: {resp.json()}")
            return True
        elif resp.status_code == 404:
            print("   ❌ مسیر /calculations/save پیدا نشد!")
            print("   ▶ مسیر در app.py تعریف نشده است")
            return False
        elif resp.status_code == 401:
            print("   ❌ توکن نامعتبر یا منقضی")
            return False
        else:
            print(f"   ❌ خطا: {resp.status_code}")
            print(f"   پاسخ: {resp.text[:200]}")
            return False
    except requests.ConnectionError:
        print("   ❌ اتصال به سرور برقرار نشد!")
        return False
    except Exception as e:
        print(f"   ❌ خطا: {e}")
        return False


# ============================================================
# 6. تست دریافت تاریخچه
# ============================================================
def test_history(token):
    print("\n📜 6. تست دریافت تاریخچه:")

    if not token:
        print("   ❌ توکن وجود ندارد")
        return False

    headers = {"Authorization": f"Bearer {token}"}

    try:
        resp = requests.get(f"{BASE_URL}/calculations", headers=headers, timeout=5)

        if resp.status_code == 200:
            data = resp.json()
            print(f"   ✅ دریافت تاریخچه موفق")
            print(f"   تعداد: {data.get('total', 0)}")
            return True
        else:
            print(f"   ❌ خطا: {resp.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ خطا: {e}")
        return False


# ============================================================
# 7. جمع‌بندی نهایی
# ============================================================
def main():
    print("=" * 60)
    print("🧪 دیاگنوستیک کامل سیستم")
    print("=" * 60)

    results = {}

    # 1. دیتابیس
    results['database'] = check_database()

    # 2. سرور
    results['server'] = check_server()

    if not results['server']:
        print("\n" + "=" * 60)
        print("❌ سرور در دسترس نیست!")
        print("▶  دستور: cd backend && python app.py")
        print("=" * 60)
        return

    # 3. احراز هویت
    token = test_auth()
    results['auth'] = token is not None

    # 4. محاسبه
    result = test_calculation(token)
    results['calculation'] = result is not None

    # 5. ذخیره (مهم)
    results['save'] = test_save(token, result)

    # 6. تاریخچه
    results['history'] = test_history(token)

    # ============================================================
    # گزارش نهایی
    # ============================================================
    print("\n" + "=" * 60)
    print("📊 گزارش نهایی")
    print("=" * 60)

    for key, value in results.items():
        icon = "✅" if value else "❌"
        print(f"  {icon} {key}")

    print("=" * 60)

    if all(results.values()):
        print("🎉 همه چیز درست کار می‌کند!")
        print("▶ مشکل از فرانت‌اند است (احتمالا CORS یا آدرس API)")
    elif not results['server']:
        print("❌ سرور روشن نیست → cd backend && python app.py")
    elif not results['save']:
        print("❌ مشکل در مسیر /calculations/save")
        print("▶ مسیر را در app.py اضافه کنید")
    elif not results['database']:
        print("❌ مشکل در دیتابیس")
        print("▶ دیتابیس را ریست کنید: حذف instance/database.db")
    else:
        print("❌ چندین مشکل وجود دارد")

    print("=" * 60)


if __name__ == "__main__":
    main()
