# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='Anonymous')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

@app.route('/')
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('home.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        new_post = Post(title=title, content=content, author=author)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# Now save the below files are in the templates folder as per given name of the files.

#<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Flask Blog</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="{{ url_for('home') }}">Flask Blog</a>
        <div class="navbar-nav">
            <a class="nav-item nav-link" href="{{ url_for('home') }}">Home</a>
            <a class="nav-item nav-link" href="{{ url_for('create') }}">New Post</a>
            <a class="nav-item nav-link" href="{{ url_for('about') }}">About</a>
        </div>
    </nav>
    <div class="container mt-4">
        {% block content %}{% endblock %}
    </div>
</body>
</html>

#<!-- templates/home.html -->
{% extends "base.html" %}
{% block content %}
    {% for post in posts %}
        <div class="card mb-4">
            <div class="card-body">
                <h2 class="card-title"><a href="{{ url_for('post', post_id=post.id) }}">{{ post.title }}</a></h2>
                <p class="card-text text-muted">By {{ post.author }} on {{ post.date_posted.strftime('%B %d, %Y') }}</p>
                <p class="card-text">{{ post.content[:200] }}...</p>
                <a href="{{ url_for('post', post_id=post.id) }}" class="btn btn-primary">Read More</a>
            </div>
        </div>
    {% endfor %}
{% endblock %}


#<!-- templates/post.html -->
{% extends "base.html" %}
{% block content %}
    <div class="card">
        <div class="card-body">
            <h2 class="card-title">{{ post.title }}</h2>
            <p class="card-text text-muted">By {{ post.author }} on {{ post.date_posted.strftime('%B %d, %Y') }}</p>
            <p class="card-text">{{ post.content }}</p>
        </div>
    </div>
    <a href="{{ url_for('home') }}" class="btn btn-secondary mt-3">Back to Home</a>
{% endblock %}


# <!-- templates/create.html -->
{% extends "base.html" %}
{% block content %}
    <h1>New Post</h1>
    <form method="POST">
        <div class="form-group">
            <label for="title">Title</label>
            <input type="text" class="form-control" id="title" name="title" required>
        </div>
        <div class="form-group">
            <label for="author">Author</label>
            <input type="text" class="form-control" id="author" name="author">
        </div>
        <div class="form-group">
            <label for="content">Content</label>
            <textarea class="form-control" id="content" name="content" rows="5" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Post</button>
    </form>
{% endblock %}

#<!-- templates/about.html -->
{% extends "base.html" %}
{% block content %}
    <h1>About</h1>
    <p>This is a simple blog application built with Flask.</p>
{% endblock %}
