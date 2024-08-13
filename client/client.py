from flask import Flask, jsonify
import httpx
from flask_cors import CORS
import logging
import time

# Configure logging
logging.basicConfig(filename='clinet_server_status.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Update these URLs based on your environment
server1_url = 'http://127.0.0.1:44271/'  
server2_url = 'http://127.0.0.1:44619/'  

# Create a global HTTP/2 client
client = httpx.Client(http2=True)

@app.route('/', methods=['GET'])
def home():
    return "Client is UP"

@app.route('/status', methods=['GET'])
def status():
    statuses = {}

    # Check Server 1
    time.sleep(1)
    try:
        response1 = client.get(server1_url)
        response1.raise_for_status()  # Raise an HTTPError for bad responses
        server1_status = response1.text
        logger.info("Server 1 is up.")
    except httpx.HTTPStatusError as e:
        server1_status = f"Server 1 returned an error: {e}"
        logger.error(f"Server 1 error: {e}")
    except httpx.RequestError:
        server1_status = "Server 1 is down"
        logger.error("Server 1 is down.")

    statuses['server1_status'] = server1_status

    
    time.sleep(1)

    # Check Server 2
    try:
        response2 = client.get(server2_url)
        response2.raise_for_status()  
        server2_status = response2.text
        logger.info("Server 2 is up.")
    except httpx.HTTPStatusError as e:
        server2_status = f"Server 2 returned an error: {e}"
        logger.error(f"Server 2 error: {e}")
    except httpx.RequestError:
        server2_status = "Server 2 is down"
        logger.error("Server 2 is down.")

    statuses['server2_status'] = server2_status

    return jsonify(statuses)

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100,debug=True)
