"""Run Data Streaming Client."""

import os
import sys
import subprocess
from config import Config

config = Config()


def run_etl():
    """
    Conditionally run the data streaming client as a subprocess.
    """
    try:
        # Change the working directory
        project_home = config.get_config_value("PROJECT_HOME")
        etl_directory = config.get_config_value("ETL_DIRECTORY")
        etl_entrypoint = config.get_config_value("ETL_ENTRYPOINT")
        os.chdir(etl_directory)

        # Start data streaming client
        result = subprocess.run(["bash", etl_entrypoint], check=True)

        # Return the exit code of the subprocess
        etl_exitcode = result.returncode

        # Step out of the etl directory
        os.chdir(project_home)
        
        if etl_exitcode == 0:
            print(r"Data Streaming Client running ...")

        else:
            print(
                f"Data Streaming Client execution failed with an exit status of {etl_exitcode}"
            )
            sys.exit(etl_exitcode)

    except FileNotFoundError:
        print("Directory not found:", etl_directory)
    except OSError as error_msg:
        print("Error:", error_msg)
