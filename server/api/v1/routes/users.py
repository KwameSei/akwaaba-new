#!/usr/bin/env python3
""" Creating user routes """

from api.v1.routes import views
import datetime
from flask import jsonify, json, make_response, request
from models.engine.database import Session
from models.user import User

db=Session()

@views.route('/hello', methods=['GET'], strict_slashes=False)
def Hello():
    return 'Hello World'

@views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Get all users"""
    users = db.query.order_by(User.id.asc()).all()

    user_list = []
    for user in users:
        user_dict = user.to_dict()
        user_list.append(user_dict)

    # Serialize the list of dictionaries to JSON and return the response
    response_data = json.dumps(user_list, default=str)
    return make_response(response_data, 200)

@views.route('/single_user/<int:id>', methods=['GET'], strict_slashes=False)
def get_user(id):
    """Get a single user by their id"""
    user=db.query(User).get(id)
    if user is not None:
        user_dict = user.to_dict()
        return jsonify(user_dict)
    else:
        return jsonify({'error': 'User not found'})

@views.route('/user', methods=["POST"], strict_slashes=False)
def create_user():
    email = request.json.get('email')
    password = request.json.get('password')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    phone = request.json.get('phone')
    address = request.json.get('address')
    status = request.json.get('status')
    # created_at = datetime.utcnow()
    # updated_at = datetime.utcnow()

    # get the current timestamp for created_at and updated_at
    current_timestamp = datetime.datetime.utcnow()

    new_user = User(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        address=address,
        status=status,
        created_at=current_timestamp,
        updated_at=current_timestamp
    )

    try:
        db.add(new_user)
        db.commit()
        # Return serialized object
        response_object = {
            'message': 'User created successfully',
            'id': new_user.id,
            'email': new_user.email,
            'password': new_user.password,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'phone': new_user.phone,
            'address': new_user.address,
            'status': new_user.status,
            'created_at': new_user.created_at,
            'updated_at': new_user.updated_at
        }
        return make_response(jsonify(response_object), 201)
        #return make_response(jsonify({"message": "Event created successfully"}), 201)
    except:
        db.rollback()
        return make_response(jsonify({"message": "Unable to create user"}), 500)
    
@views.route('/update_user/<int:id>', methods=['PUT'], strict_slashes=False)
def update_user(id):
    """Update a user by their id"""
    user = db.query(User).get(id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    # get the request data
    data = request.get_json()

    # update the user attributes
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.phone = data.get('phone', user.phone)
    user.address = data.get('address', user.address)
    user.status = data.get('status', user.status)
    user.created_at = data.get('created_at', user.created_at)
    user.updated_at = data.get('updated_at', user.updated_at)

    db.add(user)
    db.commit()

    return jsonify({'message': 'User updated successfully', 'user': user.to_dict()})

@views.route('/delete_user/<int:id>', methods=['DELETE'], strict_slashes=False)
def single_user(id):
    user = db.query(User).get(id)
    user.delete()
    return user