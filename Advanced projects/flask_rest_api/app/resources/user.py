from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models.user import User
from app.extensions import db, ma
from app.utils.helpers import error_response

user_api_bp = Blueprint('user_api', __name__)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        
    id = ma.auto_field()
    email = ma.auto_field()
    username = ma.auto_field()
    name = ma.auto_field()
    is_active = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserCreateSchema(ma.Schema):
    email = ma.String(required=True)
    username = ma.String(required=True)
    name = ma.String(required=False)
    password = ma.String(required=True)


user_create_schema = UserCreateSchema()


@user_api_bp.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    users = User.get_all()
    return jsonify({"users": users_schema.dump(users)}), 200


@user_api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID"""
    user = User.find_by_id(user_id)
    if not user:
        return error_response("User not found", 404)
    
    return jsonify({"user": user_schema.dump(user)}), 200


@user_api_bp.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        errors = user_create_schema.validate(data)
        if errors:
            return error_response(f"Validation error: {errors}", 400)
        
        # Check if username or email already exists
        if User.find_by_username(data['username']):
            return error_response("Username already exists", 409)
        
        if User.find_by_email(data['email']):
            return error_response("Email already exists", 409)
        
        # In a real app, you would hash the password here
        # For example: data['password_hash'] = hash_password(data['password'])
        # And delete the plain text password
        
        # For this example, we'll just save the password as hash
        new_user = User(
            email=data['email'],
            username=data['username'],
            name=data.get('name', ''),
            password_hash=data['password']  # In reality, would be hashed!
        )
        
        new_user.save()
        return jsonify({"message": "User created successfully", "user": user_schema.dump(new_user)}), 201
        
    except Exception as e:
        return error_response(f"Error creating user: {str(e)}", 500)


@user_api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user"""
    user = User.find_by_id(user_id)
    if not user:
        return error_response("User not found", 404)
    
    try:
        data = request.get_json()
        
        # Update fields if they exist in the request
        if 'email' in data:
            # Check if the new email is already taken by another user
            existing_user = User.find_by_email(data['email'])
            if existing_user and existing_user.id != user_id:
                return error_response("Email already exists", 409)
            user.email = data['email']
            
        if 'username' in data:
            # Check if the new username is already taken by another user
            existing_user = User.find_by_username(data['username'])
            if existing_user and existing_user.id != user_id:
                return error_response("Username already exists", 409)
            user.username = data['username']
            
        if 'name' in data:
            user.name = data['name']
            
        if 'is_active' in data:
            user.is_active = data['is_active']
        
        user.save()
        return jsonify({"message": "User updated successfully", "user": user_schema.dump(user)}), 200
        
    except Exception as e:
        return error_response(f"Error updating user: {str(e)}", 500)


@user_api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    user = User.find_by_id(user_id)
    if not user:
        return error_response("User not found", 404)
    
    try:
        user.delete()
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return error_response(f"Error deleting user: {str(e)}", 500)