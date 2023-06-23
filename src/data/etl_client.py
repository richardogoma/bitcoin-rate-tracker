"""Run Data Streaming Client."""

import os
import sys
import subprocess
from config import Config

config = Config()


def run_etl() -> bool:
    """
    Conditionally run the data streaming client as a subprocess.
    """
    try:
        # Change the working directory
        project_home = config.get_config_value("PROJECT_HOME")
        etl_directory = config.get_config_value("ETL_DIRECTORY")
        os.chdir(etl_directory)

        # Start data streaming client
        etl_entrypoint = config.get_config_value("ETL_ENTRYPOINT")
        result = subprocess.run(["bash", etl_entrypoint], check=True)

        etl_exitcode = result.returncode
        if etl_exitcode == 0:
            print(r"Data Streaming Client running ...")
            os.chdir(project_home)

        else:
            print(
                f"Data Streaming Client execution failed with an exit status of {etl_exitcode}"
            )
            os.chdir(project_home)
            sys.exit(etl_exitcode)

    except FileNotFoundError:
        print("Directory not found:", etl_directory)
    except OSError as error_msg:
        print("Error:", error_msg)
