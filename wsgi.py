#!/usr/bin/env python3
"""A web application or microservice for tracking and visualizing 
Bitcoin rates across major currencies.
"""

import os

# import sys
import subprocess
import time
from config import Config

config = Config()

if __name__ == "__main__":
    try:
        # Change the working directory
        ETL_DIRECTORY = config.get_config_value("ETL_DIRECTORY")
        os.chdir(ETL_DIRECTORY)
        print("Working directory changed to:", os.getcwd())

        # Start data streaming client
        # ETL_ENTRYPOINT = sys.argv[1]
        ETL_ENTRYPOINT = config.get_config_value("ETL_ENTRYPOINT")
        result = subprocess.run(["bash", ETL_ENTRYPOINT], check=True)

        etl_exitcode = result.returncode
        if etl_exitcode == 0:
            print(r"Data Streaming Client started successfully ...")

        else:
            print(
                f"Data Streaming Client execution failed with an exit status of {etl_exitcode}"
            )

        time.sleep(60)

    except FileNotFoundError:
        print("Directory not found:", ETL_DIRECTORY)
    except OSError as error_msg:
        print("Error:", error_msg)

    # Start Flask server
    if etl_exitcode == 0:
        HOST_NAME = config.get_config_value("HOST")
        PORT_NAME = config.get_config_value("PORT")
        PROJECT_HOME = config.get_config_value("PROJECT_HOME")

        os.chdir(PROJECT_HOME)
        print("Working directory changed to:", os.getcwd())

        from web_app import create_app

        app = create_app()
        app.run(host=HOST_NAME, port=PORT_NAME)
