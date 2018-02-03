import os

from app import app
from flask import jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
from views.authorization import login_required

# File upload configuration
UPLOAD_FOLDER = "files"
UPLOAD_FOLDER = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1 MB


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(["jpg", "png"])
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/api/file", methods=["POST"])
@login_required
def images_upload(username):
    if "file" not in request.files or request.files["file"].filename == '':
        return jsonify({"error": "No file specified"})
    file = request.files["file"]
    if file and allowed_file(file.filename):
        filename = secure_filename(username + "_" + file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

    return jsonify({
        "uploaded": True,
        "filename": filename
    })