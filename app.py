from flask_cors import CORS
from flask import Flask, jsonify, request, send_from_directory, send_file
from generate_patients import generate_patients_with_gemini
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Serve frontend page"""
    return send_file('frontend/index.html')

@app.route('/generate_patients', methods=['GET'])
def generate_patients():
    count = int(request.args.get('count', 10))
    raw_text, patients = generate_patients_with_gemini(count)
    if patients and isinstance(patients, list):
        return jsonify(patients)
    else:
        return jsonify({"error": "Failed to generate patients data"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)