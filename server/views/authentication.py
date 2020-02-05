import jwt

from flask import jsonify, request
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

from app import app


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

    # Hash password with sha256
    hashed_password = generate_password_hash(request.json.get("password"))

    new_user = User(
        username=request.json.get("username"),
        email=request.json.get("email"),
        password=hashed_password
    ).save()

    token = jwt.encode({
        "username": new_user.username,
        "email": new_user.email,
        "password": new_user.password,
        "created": str(new_user.created)
    }, app.config["SECRET_KEY"])

    return jsonify({
        "success": True,
        "user": {
            "username": new_user.username,
            "email": new_user.email,
            "password": new_user.password,
            "created": str(new_user.created)
        },
        "token": token.decode("UTF-8")
    })


@app.route("/api/login", methods=["POST"])
def login():
    if not request.json.get("username"):
        return jsonify({"error": "Username not specified"}), 409
    if not request.json.get("password"):
        return jsonify({"error": "Password not specified"}), 409

    users = User.objects(username=request.json.get("username"))

    if len(users) == 0:
        return jsonify({"error": "User not found"}), 403

    user = users.first()

    if not check_password_hash(user.password, request.json.get("password")):
        return jsonify({"error": "Invalid password"}), 401

    token = jwt.encode({
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "created": str(user.created)
    }, app.config["SECRET_KEY"])

    return jsonify({
        "success": True,
        "user": {
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "created": str(user.created)
        },
        "token": token.decode("UTF-8")
    })
