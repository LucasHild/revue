import json

from app import app
from flask import jsonify, request
from models import Post, User
from mongoengine.errors import ValidationError


@app.route("/api/posts")
def posts_index():
    posts = Post.objects()
    return jsonify([
        {
            "id": str(post.id),
            "title": post.title,
            "content": post.content,
            "user": {
                "id": str(post.user.id),
                "username": post.user.username
            },
            "comments": post.comments,
            "created": post.created.strftime("%Y-%m-%d %H:%M:%S")
        } for post in posts
    ])


@app.route("/api/posts", methods=["POST"])
def posts_create():
    if not request.json.get("title"):
        return jsonify({"error": "Title not specified"}), 409
    if not request.json.get("content"):
        return jsonify({"error": "Content not specified"}), 409

    lucas = User.objects(username="Lucas").first()

    post = Post(
        title=request.json.get("title"),
        content=request.json.get("content"),
        user=lucas,
        comments=[]
    ).save()

    return jsonify({
        "id": str(post.id),
        "title": post.title,
        "content": post.content,
        "user": {
            "id": str(post.user.id),
            "username": post.user.username
        },
        "comments": post.comments,
        "created": post.created.strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/api/posts/id/<string:id>")
def posts_item(id):
    try:
        post = Post.objects(pk=id).first()
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    return jsonify({
        "id": str(post.id),
        "title": post.title,
        "content": post.content,
        "user": {
            "id": str(post.user.id),
            "username": post.user.username
        },
        "comments": post.comments,
        "created": post.created.strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/api/posts/user/<string:username>")
def posts_user(username):
    try:
        user = User.objects(username=username).first()
    except ValidationError:
        return jsonify({"error": "User not found"}), 404

    posts = Post.objects(user=user)

    return jsonify([
        {
            "id": str(post.id),
            "title": post.title,
            "content": post.content,
            "user": {
                "id": str(post.user.id),
                "username": post.user.username
            },
            "comments": post.comments,
            "created": post.created.strftime("%Y-%m-%d %H:%M:%S")
        } for post in posts
    ])


