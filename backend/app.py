from flask import Flask, jsonify, request
from flask_cors import CORS
from core import PhysiologyEngine  # تغییر مسیر import
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, origins='*')
engine = PhysiologyEngine()

request_count = {}
MAX_REQUESTS_PER_MINUTE = 30

def rate_limit_check(ip):
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    key = f"{ip}_{now}"
    if key not in request_count:
        request_count[key] = 0
    request_count[key] += 1
    if len(request_count) > 1000:
        for k in list(request_count.keys()):
            if k.split('_')[1] != now.split(' ')[1]:
                del request_count[k]
    return request_count[key] <= MAX_REQUESTS_PER_MINUTE

@app.route('/')
def home():
    return jsonify({'message': 'سیستم تغذیه توت فرنگی آماده است!'})

@app.route('/calculate', methods=['POST'])
def calculate():
    ip = request.remote_addr
    if not rate_limit_check(ip):
        logger.warning(f"Rate limit exceeded for IP: {ip}")
        return jsonify({'error': 'تعداد درخواست‌ها بیش از حد مجاز است. لحظاتی بعد تلاش کنید.'}), 429

    try:
        data = request.json
        logger.info(f"Calculate request from {ip}: {data}")
        if not data:
            return jsonify({'error': 'داده‌ای ارسال نشده است'}), 400
        result = engine.calculate(data)
        if 'errors' in result:
            logger.warning(f"Validation errors for {ip}: {result['errors']}")
            return jsonify({'errors': result['errors']}), 400
        logger.info(f"Calculation successful for {ip}")
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error in calculate: {str(e)}")
        return jsonify({'error': 'خطای داخلی سرور. لطفاً دوباره تلاش کنید.'}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
