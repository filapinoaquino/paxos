from flask import Flask, request, abort
import hashlib
import redis
import json
import ssl
from logging.config import dictConfig

app = Flask(__name__)
conn = redis.Redis(host='redis-dev', port=6379, db=0)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

@app.route('/messages', methods = ['POST'])
def messages():
    """ Transform incoming string into 256 hash digest

        Args:
            String

        Return:
            json string with sha 256 hash digest (hexadecimal format)
    """
    request_json = request.get_json(force=True)
    message = request_json["message"]
    digest = hashlib.sha256(message).hexdigest()
    conn.set(digest, message)
    new_message = {
        "digest": digest
    }
    return json.dumps(new_message), 201
  

@app.route('/messages/<digest>')
def decode(digest):
    """ query for messages

        Args:
            String

        Return:
            json string with message value or 404 if hex digest is not found
    """ 

    message = conn.get(digest)
    if message is None:
        abort(404)
    decoded = {
        "message": message
    }
    return json.dumps(decoded)

if __name__ == "__main__":

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('localhost.crt', 'localhost.key')    
    app.run(host='0.0.0.0', port=5000, ssl_context=context, threaded=True)     