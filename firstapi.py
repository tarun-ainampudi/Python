import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api/get_ip', methods=['GET'])
def get_ip():
    # Retrieve the client's IP address
    ip_address = request.remote_addr
    
    # If behind a reverse proxy, use the X-Forwarded-For header
    if 'X-Forwarded-For' in request.headers:
        ip_address = request.headers['X-Forwarded-For']
    
    # Return the IP address as JSON
    return jsonify({'ip_address': ip_address})

if __name__ == '__main__':
    app.run(debug=True)
