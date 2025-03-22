from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 

@app.route('/api/ERA-AI', methods=['GET'])
def test():
    return jsonify({'message':'Hi there'})

if __name__ == "__main__":
    app.run(port=5000)