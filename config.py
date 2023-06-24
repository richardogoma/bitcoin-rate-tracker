"""Flask app configurations."""


class Config:
    """
    Configuration class for the application.
    """

    DEBUG = True
    DATABASE_URI = "./data_streaming_client/data/processed/bitcoin_rate_tracker.db"
    TEST_DATABASE_URI = "./data/bitcoin_rate_tracker.db"
    HOST = "127.0.0.1"
    PORT = "5051"
    PROJECT_HOME = "/workspaces/bitcoin-rate-tracker"
    ETL_DIRECTORY = "/workspaces/bitcoin-rate-tracker/data_streaming_client"
    ETL_ENTRYPOINT = "setup_etl_web_server.sh"

    def get_config_value(self, key):
        """
        Get the value of a configuration option.

        Args:
            key (str): The configuration option key.

        Returns:
            Any: The value of the configuration option.
        """
        return getattr(self, key)

    def set_config_value(self, key, value):
        """
        Set the value of a configuration option.

        Args:
            key (str): The configuration option key.
            value (Any): The value to be set for the configuration option.
        """
        setattr(self, key, value)
