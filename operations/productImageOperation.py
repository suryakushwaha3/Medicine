import os
import uuid
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}


def allowed_file(filename):
    if not filename:
        return False

    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return extension in ALLOWED_EXTENSIONS


def save_product_image(image_file, upload_folder):

    if image_file is None:
        return {
            "error": "Image file is required."
        }

    if image_file.filename == "":
        return {
            "error": "No image selected."
        }

    if not allowed_file(image_file.filename):
        return {
            "error": "Only JPG, JPEG, PNG and WEBP images are allowed."
        }

    filename = secure_filename(image_file.filename)

    extension = filename.rsplit(".", 1)[1].lower()

    unique_filename = f"{uuid.uuid4().hex}.{extension}"

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_folder,
        unique_filename
    )

    image_file.save(file_path)

    return {
        "filename": unique_filename,
        "path": file_path
    }