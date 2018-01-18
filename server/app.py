import config

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config["SECRET_KEY"] = config.flask_secret_key
CORS(app)

from views.authorization import *
from views.posts import *

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "error": "API endpoint not found"
    }), 404

@app.errorhandler(500)
@app.errorhandler(405)
def internal_server_error(e):
    return jsonify({
        "error": "Internal server error"
    }), 500

if __name__ == "__main__":
    app.run(debug=True)
