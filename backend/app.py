import os
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS

from core.physiology_engine import PhysiologyEngine
from auth import auth_bp, token_required, get_current_user_id
from database import init_db, save_calculation, get_user_calculations, get_calculation_stats

# ============================================================
# تنظیمات
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
    if not data:
        return False, 'داده اي ارسال نشده است'

    for field in REQUIRED_FIELDS:
        if field not in data:
            return False, f'فيلد {field} الزامي است'

    for field in NUMERIC_FIELDS:
        if field in data and data[field] is not None:
            try:
                float(data[field])
            except (TypeError, ValueError):
                return False, f'مقدار {field} بايد عددي باشد'

    weather = data.get('weather')
    if weather and weather not in ('sunny', 'cloudy', 'partly_cloudy'):
        return False, 'مقدار weather نامعتبر است'

    cultivar = data.get('cultivar')
    if cultivar and cultivar not in ('Albion', 'Camarosa', 'Sweet Charlie'):
        return False, 'مقدار cultivar نامعتبر است'

    return True, None


# ============================================================
# Routes
# ============================================================

@app.route('/')
def home():
    return jsonify({
        'message': 'Strawberry Nutrient System is ready!',
        'version': '1.0.0',
        'status': 'healthy',
        'auth_required': True
    })


@app.route('/calculate', methods=['POST'])
@token_required
def calculate():
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
        return jsonify({'error': 'خطاي داخلي سرور', 'detail': str(e)}), 500


# ============================================================
# ✅ مسیرهای مدیریت محاسبات (اضافه شد)
# ============================================================

@app.route('/calculations/save', methods=['POST'])
@token_required
def save_calculation_route():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({'error': 'داده اي ارسال نشده است'}), 400

    result = data.get('result')
    input_data = data.get('input_data', {})

    if not result:
        return jsonify({'error': 'نتيجه محاسبه ارسال نشده است'}), 400

    user_id = get_current_user_id()

    try:
        success = save_calculation(user_id, result, input_data)
        if success:
            return jsonify({'message': 'محاسبه با موفقيت ذخيره شد', 'status': 'success'})
        else:
            return jsonify({'error': 'خطا در ذخيره محاسبه'}), 500
    except Exception as e:
        return jsonify({'error': f'خطا: {str(e)}'}), 500


@app.route('/calculations', methods=['GET'])
@token_required
def get_calculations():
    user_id = get_current_user_id()
    limit = request.args.get('limit', 10, type=int)
    calculations = get_user_calculations(user_id, limit)
    return jsonify({'calculations': calculations, 'total': len(calculations)})


@app.route('/calculations/stats', methods=['GET'])
@token_required
def get_stats():
    user_id = get_current_user_id()
    stats = get_calculation_stats(user_id)
    return jsonify(stats)


@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'auth_required': True, 'version': '1.0.0'})


# ============================================================
# اجرا
# ============================================================
if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    port = int(os.environ.get('FLASK_PORT', 5000))

    print("=" * 60)
    print("Strawberry Nutrient System - Server Starting...")
    print("=" * 60)
    print(f"Authentication: Enabled (JWT)")
    print(f"Database: {os.environ.get('DATABASE_PATH', 'instance/database.db')}")
    print(f"Calculations: Manual save enabled")
    print(f"Server running on http://127.0.0.1:{port}")
    print("=" * 60)

    app.run(debug=debug_mode, port=port)    
