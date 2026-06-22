import os
import re
from datetime import datetime, timedelta, timezone
from functools import wraps

import jwt
from flask import Blueprint, g, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

from database import get_connection

# ============================================================
# تنظیمات احراز هویت
# ============================================================
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

JWT_SECRET = os.environ.get('JWT_SECRET', 'dev-secret-change-me')
JWT_ALGORITHM = 'HS256'
TOKEN_EXPIRY_HOURS = int(os.environ.get('JWT_EXPIRY_HOURS', 24))

# ============================================================
# اعتبارسنجی
# ============================================================
EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
USERNAME_RE = re.compile(r'^[A-Za-z0-9_]{3,32}$')


# ============================================================
# توابع کمکی
# ============================================================

def _generate_token(user_id):
    """تولید توکن JWT برای کاربر"""
    payload = {
        'user_id': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(hours=TOKEN_EXPIRY_HOURS),
        'iat': datetime.now(timezone.utc),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def _serialize_user(row):
    """تبدیل ردیف کاربر به دیکشنری"""
    return {
        'id': row['id'],
        'username': row['username'],
        'email': row['email'],
        'created_at': row['created_at'],
    }


def get_current_user_id():
    """دریافت ID کاربر فعلی از g"""
    return g.current_user['id'] if hasattr(g, 'current_user') else None


# ============================================================
# دکوراتور احراز هویت
# ============================================================

def token_required(f):
    """دکوراتور برای محافظت از مسیرها با توکن JWT"""
    @wraps(f)
    def decorated(*args, **kwargs):
        header = request.headers.get('Authorization', '')
        if not header.startswith('Bearer '):
            return jsonify({'error': 'توکن احراز هویت ارسال نشده است'}), 401

        token = header.split(' ', 1)[1].strip()

        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'توکن منقضی شده است، دوباره وارد شوید'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'توکن نامعتبر است'}), 401

        conn = get_connection()
        try:
            user = conn.execute(
                'SELECT * FROM users WHERE id = ?', (payload['user_id'],)
            ).fetchone()
        finally:
            conn.close()

        if user is None:
            return jsonify({'error': 'کاربر یافت نشد'}), 401

        g.current_user = user
        return f(*args, **kwargs)

    return decorated


# ============================================================
# مسیرهای احراز هویت
# ============================================================

@auth_bp.route('/register', methods=['POST'])
def register():
    """ثبت‌نام کاربر جدید"""
    data = request.get_json(silent=True) or {}
    username = (data.get('username') or '').strip()
    email = (data.get('email') or '').strip().lower()
    password = data.get('password') or ''

    if not USERNAME_RE.match(username):
        return jsonify({'error': 'نام کاربری باید ۳ تا ۳۲ کاراکتر و شامل حروف انگلیسی، عدد یا _ باشد'}), 400
    if not EMAIL_RE.match(email):
        return jsonify({'error': 'ایمیل نامعتبر است'}), 400
    if len(password) < 6:
        return jsonify({'error': 'رمز عبور باید حداقل ۶ کاراکتر باشد'}), 400

    conn = get_connection()
    try:
        existing = conn.execute(
            'SELECT id FROM users WHERE username = ? COLLATE NOCASE OR email = ? COLLATE NOCASE',
            (username, email),
        ).fetchone()
        if existing is not None:
            return jsonify({'error': 'نام کاربری یا ایمیل قبلاً ثبت شده است'}), 409

        cursor = conn.execute(
            'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
            (username, email, generate_password_hash(password)),
        )
        conn.commit()
        user = conn.execute(
            'SELECT * FROM users WHERE id = ?', (cursor.lastrowid,)
        ).fetchone()
    finally:
        conn.close()

    token = _generate_token(user['id'])
    return jsonify({'token': token, 'user': _serialize_user(user)}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """ورود کاربر"""
    data = request.get_json(silent=True) or {}
    identifier = (data.get('username') or data.get('email') or '').strip()
    password = data.get('password') or ''

    if not identifier or not password:
        return jsonify({'error': 'نام کاربری و رمز عبور الزامی است'}), 400

    conn = get_connection()
    try:
        user = conn.execute(
            'SELECT * FROM users WHERE username = ? COLLATE NOCASE OR email = ? COLLATE NOCASE',
            (identifier, identifier),
        ).fetchone()
    finally:
        conn.close()

    if user is None or not check_password_hash(user['password_hash'], password):
        return jsonify({'error': 'نام کاربری یا رمز عبور اشتباه است'}), 401

    token = _generate_token(user['id'])
    return jsonify({'token': token, 'user': _serialize_user(user)})


@auth_bp.route('/me', methods=['GET'])
@token_required
def me():
    """دریافت اطلاعات کاربر فعلی"""
    return jsonify({'user': _serialize_user(g.current_user)})
