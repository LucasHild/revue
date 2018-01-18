import json

from app import app
from flask import jsonify, request
from models import Post, User


@app.route("/api/posts")
def posts_index():
    posts = Post.objects()
    # posts = [json.loads(i.to_json()) for i in posts]
    return jsonify({
        "posts": json.loads(posts.to_json())
    })


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

    return jsonify(json.loads(post.to_json()))