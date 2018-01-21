import json

from app import app
from flask import jsonify, request
from models import Post, User, Comment
from mongoengine.errors import ValidationError
from views.authorization import login_required


@app.route("/api/posts")
def posts_index():
    posts = Post.objects().order_by("-created")
    return jsonify([
        {
            "id": str(post.id),
            "title": post.title,
            "content": post.content,
            "user": {
                "id": str(post.user.id),
                "username": post.user.username
            },
            "comments": [{
                "content": comment.content,
                "created": comment.created.strftime("%Y-%m-%d %H:%M:%S"),
                "user": {
                    "id": str(comment.user.id),
                    "username": comment.user.username
                }
            } for comment in post.comments][::-1],
            "created": post.created.strftime("%Y-%m-%d %H:%M:%S")
        } for post in posts
    ])


@app.route("/api/posts", methods=["POST"])
@login_required
def posts_create(username):
    if not request.json:
        return jsonify({"error": "Data not specified"}), 409
    if not request.json.get("title"):
        return jsonify({"error": "Title not specified"}), 409
    if not request.json.get("content"):
        return jsonify({"error": "Content not specified"}), 409

    user = User.objects(username=username).first()

    post = Post(
        title=request.json.get("title"),
        content=request.json.get("content"),
        user=user,
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
        "comments": [{
            "content": comment.content,
            "created": comment.created.strftime("%Y-%m-%d %H:%M:%S"),
            "user": {
                "id": str(comment.user.id),
                "username": comment.user.username
            }
        } for comment in post.comments][::-1],
        "created": post.created.strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/api/posts/id/<string:id>")
def posts_item(id):
    try:
        post = Post.objects(pk=id).first()

        # If post has alreay been deleted
        if not post:
            raise ValidationError
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
        "comments": [{
            "content": comment.content,
            "created": comment.created.strftime("%Y-%m-%d %H:%M:%S"),
            "user": {
                "id": str(comment.user.id),
                "username": comment.user.username
            }
        } for comment in post.comments][::-1],
        "created": post.created.strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/api/posts/user/<string:username>")
def posts_user(username):
    try:
        user = User.objects(username=username).first()
    except ValidationError:
        return jsonify({"error": "User not found"}), 404

    posts = Post.objects(user=user).order_by("-created")

    return jsonify([
        {
            "id": str(post.id),
            "title": post.title,
            "content": post.content,
            "user": {
                "id": str(post.user.id),
                "username": post.user.username
            },
            "comments": [{
                "content": comment.content,
                "created": comment.created.strftime("%Y-%m-%d %H:%M:%S"),
                "user": {
                    "id": str(comment.user.id),
                    "username": comment.user.username
                }
            } for comment in post.comments][::-1],
            "created": post.created.strftime("%Y-%m-%d %H:%M:%S")
        } for post in posts
    ])


@app.route("/api/posts/id/<string:id>", methods=["DELETE"])
@login_required
def posts_delete(username, id):
    try:
        post = Post.objects(pk=id).first()

        # If post has alreay been deleted
        if not post:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    # Check whether action was called by creator of the post
    if username != post.user.username:
        return jsonify({"error": "You are not the creator of the post"}), 401

    post_info = {
        "id": str(post.id),
        "title": post.title,
        "content": post.content,
        "user": {
            "id": str(post.user.id),
            "username": post.user.username
        },
        "comments": [{
            "content": comment.content,
            "created": comment.created.strftime("%Y-%m-%d %H:%M:%S"),
            "user": {
                "id": str(comment.user.id),
                "username": comment.user.username
            }
        } for comment in post.comments][::-1],
        "created": post.created.strftime("%Y-%m-%d %H:%M:%S")
    }

    post.delete()

    return jsonify(post_info)

@app.route("/api/posts/<string:id>/comments", methods=["POST"])
@login_required
def posts_create_comment(username, id):
    if not request.json.get('content'):
        return jsonify({"error": "No content specified"}), 409
    content = request.json.get('content')

    try:
        post = Post.objects(pk=id).first()
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    user = User.objects(username=username).first()
    comments = post.comments
    comments.append(Comment(user=user, content=content))
    post.save()

    return jsonify([{
            "content": comment.content,
            "created": comment.created.strftime("%Y-%m-%d %H:%M:%S"),
            "user": {
                "id": str(comment.user.id),
                "username": comment.user.username
            }
        } for comment in post.comments][::-1]
    )