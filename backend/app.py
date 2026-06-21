import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from physiology_engine import PhysiologyEngine
from auth import auth_bp, token_required
from database import init_db

app = Flask(__name__)

ALLOWED_ORIGINS = os.environ.get('ALLOWED_ORIGINS', 'http://localhost:5173,http://127.0.0.1:5173').split(',')
CORS(app, origins=ALLOWED_ORIGINS)

init_db()
app.register_blueprint(auth_bp)

engine = PhysiologyEngine()

REQUIRED_FIELDS = ['crown_diameter', 'plant_height', 'petiole_length', 'leaf_length', 'leaf_width', 'fruit_size']
NUMERIC_FIELDS = ['crown_diameter', 'plant_height', 'petiole_length', 'leaf_length', 'leaf_width',
                  'fruit_size', 'age_days', 'fruits_per_plant', 'temp_c', 'ec', 'ph']


def validate_input(data):
    if not data:
        return False, 'داده‌ای ارسال نشده است'

    for field in REQUIRED_FIELDS:
        if field not in data:
            return False, f'فیلد {field} الزامی است'

    for field in NUMERIC_FIELDS:
        if field in data:
            try:
                float(data[field])
            except (TypeError, ValueError):
                return False, f'مقدار {field} باید عددی باشد'

    if 'weather' in data and data['weather'] not in ('sunny', 'cloudy', 'partly_cloudy'):
        return False, 'مقدار weather نامعتبر است'

    return True, None


@app.route('/')
def home():
    return jsonify({'message': 'سیستم تغذیه توت فرنگی آماده است!'})


@app.route('/calculate', methods=['POST'])
@token_required
def calculate():
    data = request.get_json(silent=True)

    is_valid, error_msg = validate_input(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400

    try:
        result = engine.calculate(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': 'خطای داخلی سرور', 'detail': str(e)}), 500


@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(debug=debug_mode, port=port)
