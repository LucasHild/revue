from app import app
from flask import jsonify, request
from models import User


@app.route("/api/signup", methods=["POST"])
def sign_up():
    if not request.json.get("username"):
        return jsonify({"error": "Username not specified"}), 409
    if not request.json.get("email"):
        return jsonify({"error": "Email not specified"}), 409
    if not request.json.get("password"):
        return jsonify({"error": "Password not specified"}), 409

    if User.objects(username=request.json.get("username")):
        return jsonify({"error": "Username not available"}), 409
    if User.objects(email=request.json.get("email")):
        return jsonify({"error": "There is already an account with your email address"}), 409

    new_user = User(
        username=request.json.get("username"),
        email=request.json.get("email"),
        password=request.json.get("password")
    ).save()

    return jsonify({
        "success": True,
        "user": {
            "username": new_user.username,
            "created": new_user.created
        }
    })