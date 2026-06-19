from flask import Flask, jsonify, request
from flask_cors import CORS
from physiology_engine import PhysiologyEngine

app = Flask(__name__)
CORS(app, origins='*')
engine = PhysiologyEngine()

@app.route('/')
def home():
    return jsonify({'message': 'سیستم تغذیه توت فرنگی آماده است!'})

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    result = engine.calculate(data)
    return jsonify(result)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
