## Documentation: Web Application API Routes and View Functions

The `routes.py` script contains the API routes and view functions for a web application. It handles incoming requests and provides appropriate responses based on the requested API endpoints.

### API Blueprint: `api_bp`

The `api_bp` blueprint is created using Flask's `Blueprint` class. It defines the routes and view functions related to the API.

### API Endpoint: `/data` (GET)

The `/data` endpoint is used to retrieve Bitcoin rate data based on query parameters.

#### Query Parameters

- `currency` (string): A 3-letter currency code representing the desired currency for Bitcoin rates.
- `timerange` (string): A string representing the time range in hours for which to retrieve the Bitcoin rate data. It should be in the format `[number]h`, where `number` is a positive integer from 1 to 48.

#### View Function: `querydata()`

The `querydata()` function is the view function associated with the `/data` endpoint. It handles the GET requests to this endpoint.

The function performs the following steps:

1. Validates the request method. If it's not a GET request, it returns a 400 (Bad Request) response.
2. Extracts the query parameters `currency` and `timerange` from the request.
3. Validates the query parameters using regular expressions (regex) patterns.
4. Extracts the validated parameters and prepares them for data retrieval.
5. Calls the `retrieve_bitcoin_data()` function from the `pre_processor` module to retrieve the Bitcoin rate data.
6. Constructs a JSON response with the retrieved data and returns it with a 200 (OK) status code.
7. If any errors occur during the process, appropriate error messages are returned with a 400 (Bad Request) status code.

### `__init__.py` Script

The `__init__.py` script initializes the Flask app and sets up necessary configurations.

- The app is created using `Flask(__name__, instance_relative_config=False)`.
- CORS (Cross-Origin Resource Sharing) is enabled using `CORS(app)`.
- The configuration settings are loaded from the `Config` class defined in the `config` module.
- Within the app context, the API routes from the `api` module are imported and registered as blueprints.

### `wsgi.py` Script

The `wsgi.py` script is the entry point for running the web application or microservice. It creates the Flask app using the `create_app()` function from the `web_app` module and runs the app using `app.run()`.

### Dependencies

The script relies on the following dependencies:

- Flask: A micro web framework for building web applications.
- Flask-Cors: A Flask extension for handling Cross-Origin Resource Sharing.
- config: A custom module that provides configuration settings for the app.
- src.data.pre_processor: A module that contains the `retrieve_bitcoin_data()` function for retrieving Bitcoin rate data from a SQLite database.