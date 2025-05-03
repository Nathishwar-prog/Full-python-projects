import pytest
from app import create_app
from app.extensions import db
from app.models.user import User


@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def create_test_user(app):
    with app.app_context():
        user = User(
            email="test@example.com",
            username="tester",
            name="Test User",
            password_hash="test_password"  # In a real app, this would be hashed
        )
        user.save()
        return user