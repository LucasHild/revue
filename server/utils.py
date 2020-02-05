import os
import uuid
from flask import abort

import config


def save_image(image):
    if not image.filename.endswith(tuple([".jpg", ".png"])):
        abort(409, "Image is not valid")

    # Generate random filename
    filename = str(uuid.uuid4()).replace("-", "") + "." + image.filename.split(".")[-1]
    image.save(os.path.join(config.image_upload_folder, filename))
    return filename
