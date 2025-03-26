from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Replace this with actual authentication logic
    if username == 'admin' and password == 'password':
        return jsonify({'message': 'Login successful', 'status': 'success'}), 200
    else:
        return jsonify({'message': 'Invalid credentials', 'status': 'fail'}), 401

if __name__ == '__main__':
    app.run(debug=True)
