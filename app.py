from flask_cors import CORS
from flask import Flask, jsonify, request
from generate_patients import generate_patients_with_gemini

app = Flask(__name__)
CORS(app)

@app.route('/generate_patients', methods=['GET'])
def generate_patients():
    count = int(request.args.get('count', 10))
    patients = generate_patients_with_gemini(count)
    return jsonify(patients)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)