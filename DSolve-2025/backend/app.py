from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'password':
        return jsonify({'message': 'Login successful', 'status': 'success'}), 200
    else:
        return jsonify({'message': 'Invalid credentials', 'status': 'fail'}), 401

@app.route('/login-page', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the DSolve-2025 API'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)