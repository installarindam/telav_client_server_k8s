from flask import Flask
import os
import signal
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['GET'])
def mainrout():
    return "Server 2 is UP"

@app.route('/kill', methods=['GET'])
def kill():
    print("Server 2 Down Initiated")
    os.kill(os.getpid(), signal.SIGINT)
    #return may not execute
    return "Server 2 killed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

