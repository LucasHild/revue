from flask import jsonify
from app import app
from models import User


@app.route("/api/users/<string:username>")
def user_username(username: str) -> str:
    user = User.objects(username=username).first()
    if user:
        return jsonify(user.to_public_json())
    else:
        return jsonify({"error": "User not found"}), 404
