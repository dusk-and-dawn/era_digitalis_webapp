from flask import Flask, request, jsonify
from flask_cors import CORS
from josias_func import execute_program


app = Flask(__name__)
CORS(app) 

@app.route('/api/ERA-AI', methods=['GET'])
def test():
    return jsonify({'message':'Hi there'})

@app.route('/josias_code', methods=['POST', 'GET'])
def audio_transition():
    # hier kommt dein Code rein Josias 
    execute_program()
    return  #json oder html datei 


if __name__ == "__main__":
    app.run(port=5000)