#!/usr/bin/env python3
"""A web application or microservice for tracking and visualizing 
Bitcoin rates across major currencies.
"""

from web_app import app
from config import Config

config = Config()

if __name__ == "__main__":
    HOST_NAME = config.get_config_value("HOST")
    PORT_NAME = config.get_config_value("PORT")
    app.run(host=HOST_NAME, port=PORT_NAME)
