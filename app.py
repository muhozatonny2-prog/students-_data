from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Dummy database to store users
database = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    age = request.json.get('age')

    if not username or not password or not age:
        return jsonify({'message': 'Missing data!'}), 400
    if age < 18:
        return jsonify({'message': 'Age must be at least 18!'}), 400

    hashed_password = generate_password_hash(password)
    database[username] = {'password': hashed_password, 'age': age}
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = database.get(username)
    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401

if __name__ == '__main__':
    app.run(debug=True)