"""Initialize Flask app."""
from flask import Flask
from flask_cors import CORS
from web_app.api import routes as api_routes
from web_app.home import routes as home_routes


def create_app():
    """
    Create and configure the Flask app.
    """
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)
    app.config.from_object("config.Config")

    with app.app_context():
        # Register Blueprints
        app.register_blueprint(home_routes.home_bp)
        app.register_blueprint(api_routes.api_bp)

        return app
