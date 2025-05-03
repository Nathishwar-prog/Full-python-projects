from flask import Flask
from app.config import config_by_name
from app.extensions import db, ma, migrate
from app.resources.user import user_api_bp


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    app.register_blueprint(user_api_bp, url_prefix="/api/v1")
    
    @app.route('/health')
    def health_check():
        return {"status": "healthy"}, 200
    
    return app