from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(80))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(50))
    published_date = db.Column(db.Date)
    isbn = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Create database tables
with app.app_context():
    db.create_all()

# Helper functions
def token_required(f):
    def wrapper(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        current_user = User.query.filter_by(public_id=token).first()
        
        if not current_user:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    wrapper.__name__ = f.__name__
    return wrapper

# Routes
@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    users = User.query.all()
    output = []
    
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['email'] = user.email
        output.append(user_data)
    
    return jsonify({'users': output})

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    user = User.query.filter_by(public_id=public_id).first()
    
    if not user:
        return jsonify({'message': 'No user found!'})
    
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['email'] = user.email
    
    return jsonify({'user': user_data})

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_user = User(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        email=data['email'],
        password=hashed_password
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'New user created!'})

@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    user = User.query.filter_by(public_id=public_id).first()
    
    if not user:
        return jsonify({'message': 'No user found!'})
    
    user.admin = True
    db.session.commit()
    
    return jsonify({'message': 'The user has been promoted!'})

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    user = User.query.filter_by(public_id=public_id).first()
    
    if not user:
        return jsonify({'message': 'No user found!'})
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'The user has been deleted!'})

@app.route('/login')
def login():
    auth = request.authorization
    
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(email=auth.username).first()
    
    if not user:
        return jsonify({'message': 'No user found!'}), 404
    
    if check_password_hash(user.password, auth.password):
        return jsonify({'token': user.public_id})
    
    return jsonify({'message': 'Wrong credentials!'}), 401

@app.route('/book', methods=['GET'])
@token_required
def get_all_books(current_user):
    books = Book.query.filter_by(user_id=current_user.id).all()
    output = []
    
    for book in books:
        book_data = {}
        book_data['id'] = book.id
        book_data['title'] = book.title
        book_data['author'] = book.author
        book_data['published_date'] = book.published_date
        book_data['isbn'] = book.isbn
        output.append(book_data)
    
    return jsonify({'books': output})

@app.route('/book/<book_id>', methods=['GET'])
@token_required
def get_one_book(current_user, book_id):
    book = Book.query.filter_by(id=book_id, user_id=current_user.id).first()
    
    if not book:
        return jsonify({'message': 'No book found!'})
    
    book_data = {}
    book_data['id'] = book.id
    book_data['title'] = book.title
    book_data['author'] = book.author
    book_data['published_date'] = book.published_date
    book_data['isbn'] = book.isbn
    
    return jsonify(book_data)

@app.route('/book', methods=['POST'])
@token_required
def create_book(current_user):
    data = request.get_json()
    
    try:
        published_date = datetime.datetime.strptime(data['published_date'], '%Y-%m-%d').date()
    except:
        return jsonify({'message': 'Date format should be YYYY-MM-DD'}), 400
    
    new_book = Book(
        title=data['title'],
        author=data['author'],
        published_date=published_date,
        isbn=data['isbn'],
        user_id=current_user.id
    )
    
    db.session.add(new_book)
    db.session.commit()
    
    return jsonify({'message': 'Book created!'})

@app.route('/book/<book_id>', methods=['PUT'])
@token_required
def update_book(current_user, book_id):
    book = Book.query.filter_by(id=book_id, user_id=current_user.id).first()
    
    if not book:
        return jsonify({'message': 'No book found!'})
    
    data = request.get_json()
    
    if 'title' in data:
        book.title = data['title']
    if 'author' in data:
        book.author = data['author']
    if 'published_date' in data:
        try:
            book.published_date = datetime.datetime.strptime(data['published_date'], '%Y-%m-%d').date()
        except:
            return jsonify({'message': 'Date format should be YYYY-MM-DD'}), 400
    if 'isbn' in data:
        book.isbn = data['isbn']
    
    db.session.commit()
    
    return jsonify({'message': 'Book has been updated!'})

@app.route('/book/<book_id>', methods=['DELETE'])
@token_required
def delete_book(current_user, book_id):
    book = Book.query.filter_by(id=book_id, user_id=current_user.id).first()
    
    if not book:
        return jsonify({'message': 'No book found!'})
    
    db.session.delete(book)
    db.session.commit()
    
    return jsonify({'message': 'Book deleted!'})

if __name__ == '__main__':
    app.run(debug=True)
