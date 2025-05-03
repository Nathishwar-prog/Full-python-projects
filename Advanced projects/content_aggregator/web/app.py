import logging
from flask import Flask, render_template, jsonify, request
from datetime import datetime

logger = logging.getLogger(__name__)

def start_app(content):
    """Start the Flask web application to display content."""
    app = Flask(__name__)
    
    # Store content in memory (for demo purposes)
    app.config['CONTENT'] = content
    
    @app.route('/')
    def index():
        """Render the main page."""
        return render_template('index.html')
    
    @app.route('/api/content')
    def api_content():
        """API endpoint to get content with filtering and pagination."""
        content = app.config['CONTENT']
        
        # Apply filters if provided
        source_type = request.args.get('source_type')
        if source_type:
            content = [item for item in content if item.get('source_type') == source_type]
        
        keyword = request.args.get('keyword')
        if keyword:
            keyword = keyword.lower()
            content = [
                item for item in content 
                if keyword in item.get('title', '').lower() or 
                   keyword in item.get('description', '').lower()
            ]
        
        # Apply pagination
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        
        paginated_content = content[start_idx:end_idx]
        
        # Convert datetime objects to strings
        serializable_content = []
        for item in paginated_content:
            serializable_item = {}
            for key, value in item.items():
                if isinstance(value, datetime):
                    serializable_item[key] = value.isoformat()
                else:
                    serializable_item[key] = value
            serializable_content.append(serializable_item)
        
        return jsonify({
            'content': serializable_content,
            'total': len(content),
            'page': page,
            'per_page': per_page,
            'total_pages': (len(content) + per_page - 1) // per_page
        })
    
    @app.route('/api/sources')
    def api_sources():
        """API endpoint to get source types for filtering."""
        content = app.config['CONTENT']
        source_types = set(item.get('source_type') for item in content if 'source_type' in item)
        return jsonify(list(source_types))
    
    # Run the app
    logger.info("Web interface starting on http://127.0.0.1:5000")
    app.run(debug=False)