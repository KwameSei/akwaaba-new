#!/usr/bin/env python3
"""Server configuration for Flask web application"""

from models import storage
from models.event import Event
from models.user import User
from os import getenv
from flask import Flask, jsonify
from uuid import uuid4
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/home/', strict_slashes=False)
def home():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    """Main function"""
    app.run(host='0.0.0.0', port=5000, debug=True)