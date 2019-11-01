from flask import Flask
from flask import jsonify
import urllib.request
import ssl
import socket
app = Flask(__name__) 

@app.route('/')
def index():
  ssl._create_default_https_context = ssl._create_unverified_context
  data = {
    'app': 'python flask',
    'host': socket.gethostname(),
    'php': urllib.request.urlopen('https://php-service/data').read(),
    'node': urllib.request.urlopen('https://node-service/data').read(),
    'python': urllib.request.urlopen('https://python-service/data').read(),
    'externalphp': urllib.request.urlopen('https://externalphp-service/data').read(),
    'externalpython': urllib.request.urlopen('https://externalpython-service/data').read()
  }
  return jsonify(data)
  
@app.route('/data')
def data():
  data = {
    'app': 'python flask',
    'host': socket.gethostname()
  }
  return jsonify(data)