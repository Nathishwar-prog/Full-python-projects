import json
import pytest


def test_get_users(client):
    """Test getting all users"""
    response = client.get('/api/v1/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "users" in data
    assert isinstance(data["users"], list)


def test_create_user(client):
    """Test creating a new user"""
    user_data = {
        "email": "new@example.com",
        "username": "newuser",
        "name": "New User",
        "password": "password123"
    }
    
    response = client.post(
        '/api/v1/users',
        data=json.dumps(user_data),
        content_type='application/json'
    )
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert "message" in data
    assert "user" in data
    assert data["user"]["email"] == user_data["email"]
    assert data["user"]["username"] == user_data["username"]


def test_get_user(client, create_test_user):
    """Test getting a specific user"""
    test_user = create_test_user
    
    response = client.get(f'/api/v1/users/{test_user.id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "user" in data
    assert data["user"]["id"] == test_user.id
    assert data["user"]["email"] == test_user.email


def test_update_user(client, create_test_user):
    """Test updating a user"""
    test_user = create_test_user
    
    update_data = {
        "name": "Updated Name"
    }
    
    response = client.put(
        f'/api/v1/users/{test_user.id}',
        data=json.dumps(update_data),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "message" in data
    assert "user" in data
    assert data["user"]["name"] == update_data["name"]


def test_delete_user(client, create_test_user):
    """Test deleting a user"""
    test_user = create_test_user
    
    response = client.delete(f'/api/v1/users/{test_user.id}')
    assert response.status_code == 200
    
    # Verify user is deleted
    response = client.get(f'/api/v1/users/{test_user.id}')
    assert response.status_code == 404