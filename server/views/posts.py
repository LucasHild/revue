from schema import Schema, And

import utils
from app import app
from flask import jsonify, request
from models import Post, User, Comment, Subvue
from mongoengine.errors import ValidationError
from authorization import login_required


@app.route("/api/posts")
def posts_index():
    posts = Post.objects().order_by("-created")
    return jsonify([post.to_public_json() for post in posts])


@app.route("/api/posts", methods=["POST"])
@login_required
def posts_create(username: str):
    schema = Schema({
        "title": And(str, len, error="Title not specified"),
        "subvue": And(str, len, error="Subvue not specified"),
        "content": And(str, len, error="Content not specified"),
    })
    validated = schema.validate(dict(request.form))

    subvue_permalink = validated["subvue"]
    subvue = Subvue.objects(permalink__iexact=subvue_permalink).first()
    if not subvue:
        return jsonify({"error": f"Subvue '{subvue_permalink}' not found"}), 404

    user = User.objects(username=username).first()

    image = request.files.get("image")
    if image:
        image_filename = utils.save_image()

    else:
        image_filename = None

    post = Post(
        title=validated["title"],
        subvue=subvue,
        content=validated["content"],
        user=user,
        comments=[],
        image=image_filename
    ).save()

    return jsonify(post.to_public_json())


@app.route("/api/posts/id/<string:id>")
def posts_item(id: str):
    try:
        post = Post.objects(pk=id).first()

        # If post has alreay been deleted
        if not post:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    return jsonify(post.to_public_json())


@app.route("/api/posts/user/<string:username>")
def posts_user(username: str):
    try:
        user = User.objects(username=username).first()
    except ValidationError:
        return jsonify({"error": "User not found"}), 404

    posts = Post.objects(user=user).order_by("-created")

    return jsonify([post.to_public_json() for post in posts])


@app.route("/api/posts/id/<string:id>", methods=["DELETE"])
@login_required
def posts_delete(username: str, id: str):
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

    post_info = post.to_public_json()

    post.delete()

    return jsonify(post_info)


@app.route("/api/posts/<string:id>/comments", methods=["POST"])
@login_required
def posts_create_comment(username: str, id: str):
    schema = Schema({
        "content": And(str, len, error="No content specified")
    })
    validated = schema.validate(request.json)

    try:
        post = Post.objects(pk=id).first()
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    user = User.objects(username=username).first()
    comments = post.comments
    comments.append(Comment(user=user, content=validated["content"]))
    post.save()

    return jsonify([comment.to_public_json() for comment in post.comments][::-1])


@app.route("/api/posts/<string:id>/upvote", methods=["POST"])
@login_required
def posts_upvote(username: str, id: str):
    try:
        post = Post.objects(pk=id).first()
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    user = User.objects(username=username).first()

    upvotes = post.upvotes
    downvotes = post.downvotes

    if username in [u["username"] for u in upvotes]:
        # User already upvotes
        upvote_index = [d.username for d in upvotes].index(username)
        upvotes.pop(upvote_index)
    elif username in [u["username"] for u in downvotes]:
        # User already downvoted
        downvote_index = [d.username for d in downvotes].index(username)
        downvotes.pop(downvote_index)
        upvotes.append(user)
    else:
        upvotes.append(user)

    post.save()

    return jsonify({
        "upvotes": post.to_public_json()["upvotes"],
        "downvotes": post.to_public_json()["downvotes"]
    })


@app.route("/api/posts/<string:id>/downvote", methods=["POST"])
@login_required
def posts_downvote(username: str, id: str):
    try:
        post = Post.objects(pk=id).first()
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    user = User.objects(username=username).first()

    upvotes = post.upvotes
    downvotes = post.downvotes

    if username in [u["username"] for u in downvotes]:
        # User already upvotes
        downvote_index = [d.username for d in downvotes].index(username)
        downvotes.pop(downvote_index)
    elif username in [u["username"] for u in upvotes]:
        upvote_index = [d.username for d in upvotes].index(username)
        upvotes.pop(upvote_index)
        downvotes.append(user)
    else:
        downvotes.append(user)

    post.save()

    return jsonify({
        "upvotes": post.to_public_json()["upvotes"],
        "downvotes": post.to_public_json()["downvotes"]
    })
