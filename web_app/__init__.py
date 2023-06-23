"""Initialize Flask app."""
from flask import Flask
from flask_cors import CORS
from web_app.api import routes as api_routes
from web_app.home import routes as home_routes
from src.data.etl_client import run_etl


app = Flask(__name__, instance_relative_config=False)


def start_etl_client():
    """Initialize data streaming client."""
    app.logger.info("Initializing the data streaming client")
    run_etl()


CORS(app)
app.config.from_object("config.Config")

# Register Blueprints
app.register_blueprint(home_routes.home_bp)
app.register_blueprint(api_routes.api_bp)

with app.app_context():
    start_etl_client()
