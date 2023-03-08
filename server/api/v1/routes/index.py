#!/usr/bin/env python3
""" Creating index for routes """

from api.v1.routes import views
import datetime
from flask import jsonify, json, make_response, request
from models.engine.database import Session
from models.event import All_Event
from models.user import User
#from models.models import User, All_Event
from typing import List
import os
from dotenv import load_dotenv
load_dotenv()
import time
from werkzeug.utils import secure_filename

# Cloudinary
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Cloudinary config
cloudinary.config(
    cloud_name = os.environ.get('CLOUDINARY_NAME'),
    api_key = os.environ.get('CLOUDINARY_API_KEY'),
    api_secret = os.environ.get('CLOUDINARY_API_SECRET')
)

db=Session()

@views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ API status """

    return make_response(jsonify({"Status": "Okay"}), 200)

# Getting events
# @views.route('/events', methods=["GET"], strict_slashes=False)
# def get_all_events():
#     All_Events=db.query(All_Event).all()
#     # return All_Events
#     return jsonify(All_Events.to_dict())

@views.route('/events', methods=["GET"], strict_slashes=False)
def get_events():
    # Query the database for all events
    events = db.query(All_Event).order_by(All_Event.id.asc()).all()

    # Create a list of dictionaries representing each event
    event_list = []
    for event in events:
        event_dict = event.to_dict()
        event_list.append(event_dict)

    # Serialize the list of dictionaries to JSON and return the response
    response_data = json.dumps(event_list, default=str)
    return make_response(response_data, 200)

@views.route('/event/{event_id}', methods=["GET"], strict_slashes=False)
def get_one_event(event_id:int):
    pass

# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# UPLOAD_FOLDER = 'uploads'

@views.route('/create_event', methods=["POST"], strict_slashes=False)
def create_event():

    # # Check if featuredImage field is present
    # if 'featuredImage' not in request.files:
    #     return make_response(jsonify({'error': 'featuredImage is required'}), 400)

    # file = request.files['image']

    # # check if the file has an allowed extension
    # ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
    # if not file or not '.' in file.filename or file.filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
    #     raise ValueError(f"Invalid file type. Allowed extensions are {', '.join(ALLOWED_EXTENSIONS)}")

    # # check if the request contains a file
    # if not file:
    #     raise ValueError("featuredImage is required")
    
    # # secure the filename and save it to the app's upload folder
    # filename = secure_filename(file.filename)
    # filename = f"{int(time.time())}_{filename}"
    # file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)
    # os.makedirs(file_dir, exist_ok=True)
    # file_path = os.path.join(file_dir, filename)
    # file.save(file_path)

    try:
        title = request.form.get('title')
        description = request.form.get('description')
        category = request.form.get('category')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        location = request.form.get('location')
        region = request.form.get('region')
        cost = request.form.get('cost')
        registration = request.form.get('registration')
        isPublic = request.form.get('isPublic')
        views = request.form.get('views')
        featuredImage = request.form.get('file')
        user_id = request.form.get('user_id')

        # get the current timestamp for created_at and updated_at
        current_timestamp = datetime.datetime.now()

        # convert registration and isPublic to boolean values
        if registration and registration.lower() == 'true':
            registration = True
        else:
            registration = False

        if isPublic and isPublic.lower() == 'true':
            isPublic = True
        else:
            isPublic = False

        if cost and isinstance(cost, str) and cost.isdigit():
            cost = int(cost)
        else:
            cost = 0

        if views and isinstance(views, str) and views.isdigit():
            views = int(views)
        else:
            views = 0

        # # # Upload image to cloudinary
        # # featuredImage = None
        # # if image:
        # #     upload_result = cloudinary.uploader.upload(image, folder='events', use_filename=True, unique_filename=False)
        # #     featuredImage = upload_result['secure_url']
        # result = cloudinary.uploader.upload(file.file)
        # featuredImage = result.get('url')
        event_dict = "Worked"
        if (featuredImage):
            # Upload image to cloudinary
            upload_response = cloudinary.uploader.upload(featuredImage, folder='events', use_filename=True, unique_filename=False)
            
            if upload_response:
                new_event = All_Event(
                    title=title,
                    description=description,
                    category=category,
                    start_date=start_date,
                    end_date=end_date,
                    location=location,
                    region=region,
                    cost=cost,
                    registration=registration,
                    isPublic=isPublic,
                    views=views,
                    featuredImage=upload_response['secure_url'],
                    created_at=current_timestamp,
                    updated_at=current_timestamp,
                    user_id=user_id
                )

                db.add(new_event)
                db.commit()

                # Convert the All_Event object to a dictionary
                event_dict = new_event.to_dict()
                #event_dict.pop('_sa_instance_state', None)
            else:
                event_dict = "An error occurred while uploading file"
        else:
                event_dict = "No file was uploaded"

                # Serialize the dictionary to JSON and return the response
        response_data = json.dumps(event_dict, default=str)
        return make_response(response_data, 200)
    except Exception as e:
        db.rollback()
        # os.remove(file_path)
        return make_response(jsonify({'error': f'An error occurred while uploading file: {str(e)}'}), 500)

# Updating events
@views.route('/event/{event_id}', methods=["PUT"], strict_slashes=False)
def update_one_event(event_id:int):
    pass

# Deleting events
@views.route('/event/{event_id}', methods=["DELETE"], strict_slashes=False)
def delete_one_event(event_id:int):
    pass