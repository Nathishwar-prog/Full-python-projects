# Flask REST API

A robust and scalable RESTful API built with Flask, SQLAlchemy, and Flask-RESTful.

## Developed by

**Nathishwar**

## Project Overview

This REST API project provides a solid foundation for building web services with Python and Flask. It includes user management endpoints with full CRUD operations, database integration, request validation, comprehensive error handling, and testing infrastructure.

## Features

- **Modular Architecture**: Well-structured project organization with separation of concerns
- **RESTful Endpoints**: Complete set of CRUD operations for user management
- **Data Validation**: Request validation using Marshmallow schemas
- **Database Integration**: SQLAlchemy ORM with migration support
- **Environment Configuration**: Support for development, testing, and production environments
- **Authentication Ready**: Structure in place to add JWT or other authentication methods
- **Comprehensive Testing**: Pytest fixtures and test cases for API endpoints
- **Error Handling**: Standardized error responses across the API

## Project Structure

```
flask_rest_api/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── resources/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── extensions.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_user_api.py
│
├── .env.example
├── requirements.txt
└── run.py
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd flask_rest_api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

## Running the Application

```bash
python run.py
```

The server will start on http://localhost:5000 by default.

## API Endpoints

### User Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/users | Get all users |
| GET | /api/v1/users/{id} | Get a specific user |
| POST | /api/v1/users | Create a new user |
| PUT | /api/v1/users/{id} | Update a user |
| DELETE | /api/v1/users/{id} | Delete a user |

### Health Check

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Check API health status |

## Example Requests

### Create a User

```bash
curl -X POST http://localhost:5000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "username123",
    "name": "Full Name",
    "password": "secure_password"
  }'
```

### Get All Users

```bash
curl -X GET http://localhost:5000/api/v1/users
```

## Running Tests

```bash
pytest
```

## Database Migrations

Initialize migrations:
```bash
flask db init
```

Create a migration:
```bash
flask db migrate -m "Initial migration"
```

Apply migrations:
```bash
flask db upgrade
```

## Future Enhancements

- Add JWT authentication
- Implement role-based access control
- Add rate limiting
- Implement caching
- Add more comprehensive logging
- Create Swagger/OpenAPI documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contact

For any questions or suggestions, please contact:
- **Nathishwar** - Project Developer