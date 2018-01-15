import config

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config["SECRET_KEY"] = config.flask_secret_key
CORS(app)

from routes.authorization import *

if __name__ == "__main__":
    app.run(debug=True)
