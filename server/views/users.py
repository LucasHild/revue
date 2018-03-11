import config
import os
import uuid

from app import app
from flask import jsonify, request
from models import Post, User, Comment, Subvue
from mongoengine.errors import ValidationError
from views.authorization import login_required


@app.route("/api/users/<string:username>")
def user_username(username):
    user = User.objects(username=username).first()
    print(user)
    if user:
        return jsonify(user.to_public_json())
    else:
        return jsonify({"error": "User not found"}), 404
