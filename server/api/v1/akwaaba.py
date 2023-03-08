#from models import storage
from os import getenv
from flask_cors import CORS
from flask import Flask, make_response, jsonify
from api.v1.routes import views

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(views)

@app.errorhandler(404)
def not_found(error):
    """ Throwing 404 error """
    return make_response(jsonify({'error': "Not Found"}))

if __name__ == "__main__":
    """ Main function"""
    host = getenv('API_HOST')
    port = getenv('API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, debug=True, threaded=True)