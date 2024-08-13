from flask import Flask
import os
import signal
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['GET'])
def mainrout():
    return "Server 1 is UP"

@app.route('/kill', methods=['GET'])
def kill():
    print("Server 1 Down Initiated")
    os.kill(os.getpid(), signal.SIGINT)
    #return may not execute
    return "Server 1 killed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
