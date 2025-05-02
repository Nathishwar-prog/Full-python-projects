import sqlite3
import random
import string
from urllib.parse import urlparse
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    
    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  original_url TEXT NOT NULL,
                  short_code TEXT UNIQUE NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  clicks INTEGER DEFAULT 0)''')
    
    conn.commit()
    conn.close()

init_db()

# Helper functions
def generate_short_code(length=6):
    """Generate a random short code for the URL"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def is_valid_url(url):
    """Check if the URL is valid"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

# Routes
@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Create a short URL from a long URL"""
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    original_url = data['url']
    
    if not is_valid_url(original_url):
        return jsonify({'error': 'Invalid URL'}), 400
    
    # Check if URL already exists in database
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    
    c.execute("SELECT short_code FROM urls WHERE original_url = ?", (original_url,))
    result = c.fetchone()
    
    if result:
        short_code = result[0]
        conn.close()
        return jsonify({
            'original_url': original_url,
            'short_url': f"{request.host_url}{short_code}",
            'message': 'URL already shortened'
        })
    
    # Generate a unique short code
    short_code = generate_short_code()
    
    # Ensure the short code is unique
    while True:
        c.execute("SELECT id FROM urls WHERE short_code = ?", (short_code,))
        if not c.fetchone():
            break
        short_code = generate_short_code()
    
    # Insert into database
    c.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)",
              (original_url, short_code))
    conn.commit()
    conn.close()
    
    return jsonify({
        'original_url': original_url,
        'short_url': f"{request.host_url}{short_code}"
    })

@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Redirect to the original URL"""
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    
    c.execute("SELECT original_url FROM urls WHERE short_code = ?", (short_code,))
    result = c.fetchone()
    
    if not result:
        conn.close()
        return jsonify({'error': 'Short URL not found'}), 404
    
    original_url = result[0]
    
    # Update click count
    c.execute("UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?", (short_code,))
    conn.commit()
    conn.close()
    
    return redirect(original_url)

@app.route('/stats/<short_code>')
def get_url_stats(short_code):
    """Get statistics for a short URL"""
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    
    c.execute("SELECT original_url, created_at, clicks FROM urls WHERE short_code = ?", (short_code,))
    result = c.fetchone()
    conn.close()
    
    if not result:
        return jsonify({'error': 'Short URL not found'}), 404
    
    original_url, created_at, clicks = result
    
    return jsonify({
        'original_url': original_url,
        'short_url': f"{request.host_url}{short_code}",
        'created_at': created_at,
        'clicks': clicks
    })

@app.route('/')
def index():
    """Display basic information about the API"""
    return """
    <h1>URL Shortener API</h1>
    <p>Endpoints:</p>
    <ul>
        <li><strong>POST /shorten</strong> - Create a short URL (requires JSON with 'url' field)</li>
        <li><strong>GET /&lt;short_code&gt;</strong> - Redirect to original URL</li>
        <li><strong>GET /stats/&lt;short_code&gt;</strong> - Get statistics for a short URL</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True)
