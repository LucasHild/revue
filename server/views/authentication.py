import jwt

from flask import jsonify, request
from models import User
from schema import Schema, Regex
from werkzeug.security import generate_password_hash, check_password_hash

from app import app

MAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


@app.route("/api/signup", methods=["POST"])
def sign_up():
    schema = Schema({
        "username": str,
        "email": Regex(MAIL_REGEX, error="Mail address is invalid"),
        "password": str
    })
    validated = schema.validate(request.json)

    if User.objects(username=validated["username"]):
        return jsonify({"error": "Username not available"}), 409
    if User.objects(email=validated["email"]):
        return jsonify({"error": "There is already an account with your email address"}), 409

    # Hash password with sha256
    hashed_password = generate_password_hash(validated["password"])

    new_user = User(
        username=validated["username"],
        email=validated["email"],
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
    schema = Schema({
        "username": str,
        "password": str
    })
    validated = schema.validate(request.json)

    users = User.objects(username=validated["username"])

    if len(users) == 0:
        return jsonify({"error": "User not found"}), 403

    user = users.first()

    if not check_password_hash(user.password, validated["password"]):
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
