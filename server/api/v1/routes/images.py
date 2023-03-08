#!/usr/bin/env python3
""" Creating Images """

import os
import time
from flask import jsonify, make_response, request
from werkzeug.utils import secure_filename
from api.v1.routes import views

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = 'uploads'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@views.route('/image_upload', methods=["POST"], strict_slashes=False)
def upload():
    try:
        if 'file' not in request.files:
            return make_response(jsonify({'error': 'No file part in the request'}), 400)

        file = request.files['file']

        if file.filename == '':
            return make_response(jsonify({'error': 'No file selected for uploading'}), 400)

        if not allowed_file(file.filename):
            return make_response(jsonify({'error': 'File type not allowed. Allowed types: png, jpg, jpeg'}), 400)

        filename = secure_filename(file.filename)
        filename = f"{int(time.time())}_{filename}"
        file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)
        os.makedirs(file_dir, exist_ok=True)
        file_path = os.path.join(file_dir, filename)
        file.save(file_path)

        response = make_response(jsonify({'message': 'File successfully uploaded', 'filename': filename}), 200)
        return response
    except Exception as e:
        return make_response(jsonify({'error': f'An error occurred while uploading file: {str(e)}'}), 500)
    
# @views.after_request
# def add_cors_headers(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
#     response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,POST'
#     return response

    # if 'file' not in request.files:
    #     return jsonify({'message': 'No file uploaded'}), 400

    # file = request.files['file']

    # if file.filename == '':
    #     return jsonify({'message': 'No file uploaded'}), 400

    # if not allowed_file(file.filename):
    #     return jsonify({'message': 'Invalid file type'}), 400

    # filename = str(time.time()) + '.' + file.filename.rsplit('.', 1)[1]
    # file_path = os.path.join('client/assets/uploads', filename)
    # file.save(file_path)

    # return jsonify({'filename': filename})

    # # Check for valid image type
    # ALLOWED_IMAGE_TYPES = {'image/png', 'image/jpg', 'image/jpeg', 'image/gif'}
    # pic = request.files.get('pic')
    # if not pic:
    #     return 'No pic uploaded', 400
    # if pic.mimetype not in ALLOWED_IMAGE_TYPES:
    #     return 'Invalid file type', 400

    # # Generate safe filename and create Images object
    # filename = secure_filename(pic.filename)
    # mimetype = pic.mimetype

    # img_data = pic.read()

    # new_image = Images(
    #     img=img_data,
    #     mimetype=mimetype,
    #     name=filename
    # )

    # # Insert into database using context manager
    # with session_scope() as db:
    #     db.add(new_image)
    #     db.commit()

    # # Return success message
    # return 'Image Successfully Added', 200

# from pathlib import Path
# from flask import Flask, jsonify, request
# from werkzeug.utils import secure_filename

# ALLOWED_FILETYPES = ["image/png", "image/jpg", "image/jpeg", "image/JPG", "image/PNG", "image/JPEG"]
# HOME = str(Path.home())
# DESTINATION_PATH = os.path.abspath(os.path.join(HOME, "my_projects/akwaaba/client/src/assets"))

# @views.route('/image_upload', methods=["POST"], strict_slashes=False)
# def Upload_Image():
#     if request.files:
#         for i, file in enumerate(request.files):
#             try:
#                 image = request.files[f"images[{i}]"]
#                 if image.content_type not in ALLOWED_FILETYPES:
#                     return jsonify("Unsupported Media Type"), 415
#                 if not os.path.exists(DESTINATION_PATH):
#                     os.makedirs(DESTINATION_PATH, exist_ok=True)
#                 image.save(os.path.join(DESTINATION_PATH, secure_filename(image.filename)))
#             except (KeyError, FileNotFoundError):
#                 return jsonify("An error occurred while processing the file."), 500
#         return jsonify("Image saved."), 200
#     return jsonify(False)