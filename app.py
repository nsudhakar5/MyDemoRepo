from flask import Flask, jsonify

app = Flask(__name__)

@route('/')
def home():
    return jsonify(status="success", message="Hello from EKS!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
