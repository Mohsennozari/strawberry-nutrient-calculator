import os
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS

from core.physiology_engine import PhysiologyEngine
from auth import auth_bp, token_required
from database import init_db

# ============================================================
# تنظیمات لاگ‌گیری
# ============================================================
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# ============================================================
# Flask App
# ============================================================
app = Flask(__name__)

ALLOWED_ORIGINS = os.environ.get('ALLOWED_ORIGINS', 'http://localhost:5173,http://127.0.0.1:5173').split(',')
CORS(app, origins=ALLOWED_ORIGINS)

# ============================================================
# دیتابیس
# ============================================================
init_db()
app.register_blueprint(auth_bp)

# ============================================================
# موتور محاسبه
# ============================================================
engine = PhysiologyEngine()

# ============================================================
# اعتبارسنجی ورودی
# ============================================================
REQUIRED_FIELDS = ['crown_diameter', 'plant_height', 'petiole_length', 'leaf_length', 'leaf_width']
NUMERIC_FIELDS = ['crown_diameter', 'plant_height', 'petiole_length', 'leaf_length', 'leaf_width',
                  'fruit_size', 'age_days', 'fruits_per_plant', 'temp_c', 'ec', 'ph']


def validate_input(data):
    """اعتبارسنجی داده‌های ورودی"""
    if not data:
        return False, 'داده‌ای ارسال نشده است'

    for field in REQUIRED_FIELDS:
        if field not in data:
            return False, f'فیلد {field} الزامی است'

    for field in NUMERIC_FIELDS:
        if field in data and data[field] is not None:
            try:
                float(data[field])
            except (TypeError, ValueError):
                return False, f'مقدار {field} باید عددی باشد'

    weather = data.get('weather')
    if weather and weather not in ('sunny', 'cloudy', 'partly_cloudy'):
        return False, 'مقدار weather نامعتبر است (sunny, cloudy, partly_cloudy)'

    cultivar = data.get('cultivar')
    if cultivar and cultivar not in ('Albion', 'Camarosa', 'Sweet Charlie'):
        return False, 'مقدار cultivar نامعتبر است (Albion, Camarosa, Sweet Charlie)'

    return True, None


# ============================================================
# Routes
# ============================================================

@app.route('/')
def home():
    return jsonify({
        'message': '🍓 سیستم تغذیه توت فرنگی آماده است!',
        'version': '1.0.0',
        'status': 'healthy',
        'auth_required': True
    })


@app.route('/calculate', methods=['POST'])
@token_required
def calculate():
    """محاسبه نیاز غذایی - نیاز به احراز هویت"""
    data = request.get_json(silent=True)

    is_valid, error_msg = validate_input(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    try:
        result = engine.calculate(data)
        if 'errors' in result:
            return jsonify({'errors': result['errors']}), 400
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'error': 'خطای داخلی سرور',
            'detail': str(e) if app.debug else None
        }), 500


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'auth_required': True,
        'version': '1.0.0'
    })


@app.route('/api/docs', methods=['GET'])
def api_docs():
    """مستندات API"""
    return jsonify({
        'name': 'Strawberry Nutrient System API',
        'version': '1.0.0',
        'description': 'سیستم تصمیم‌یار هوشمند برای محاسبه نیاز غذایی توت‌فرنگی',
        'endpoints': {
            '/': {'method': 'GET', 'description': 'صفحه اصلی'},
            '/auth/register': {'method': 'POST', 'description': 'ثبت‌نام کاربر', 'auth': False},
            '/auth/login': {'method': 'POST', 'description': 'ورود کاربر', 'auth': False},
            '/auth/me': {'method': 'GET', 'description': 'اطلاعات کاربر', 'auth': True},
            '/calculate': {'method': 'POST', 'description': 'محاسبه نیاز غذایی', 'auth': True},
            '/health': {'method': 'GET', 'description': 'وضعیت سلامت', 'auth': False},
            '/api/docs': {'method': 'GET', 'description': 'این مستندات', 'auth': False}
        }
    })


# ============================================================
# اجرای سرور
# ============================================================
if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    port = int(os.environ.get('FLASK_PORT', 5000))

    print("=" * 60)
    print("🍓 Strawberry Nutrient System - Server Starting...")
    print("=" * 60)
    print(f"🔐 Authentication: Enabled (JWT)")
    print(f"📁 Database: {os.environ.get('DATABASE_PATH', 'instance/database.db')}")
    print(f"📁 Logs: {LOG_DIR}")
    print(f"🚀 Server running on http://127.0.0.1:{port}")
    print("=" * 60)

    app.run(debug=debug_mode, port=port)
