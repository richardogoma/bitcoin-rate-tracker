## Documentation: Web Application API Routes and View Functions

The `routes.py` script contains the API routes and view functions for a web application. It handles incoming requests and provides appropriate responses based on the requested API endpoints.

### API Blueprint: `api_bp`

The `api_bp` blueprint is created using Flask's `Blueprint` class. It defines the routes and view functions related to the API.

### API Endpoint: `/data` (GET)

The `/data` endpoint is used to retrieve Bitcoin rate data based on query parameters.

#### Query Parameters

- `currency` (string): A 3-letter currency code representing the desired currency for Bitcoin rates.
- `timerange` (string): A string representing the time range in hours for which to retrieve the Bitcoin rate data. It should be in the format `[number]h`, where `number` is a positive integer from 1 to 48.

#### Usage
```bash
ping -c 4 richardogoma.pythonanywhere.com
```
<img width="623" alt="Screenshot 2023-06-22 120122" src="https://github.com/richardogoma/bitcoin-rate-tracker/assets/121939700/a2e0a837-941a-4775-9fc1-b5722e1ed5f9">

```bash
curl "https://richardogoma.pythonanywhere.com/data?currency=USD&timerange=1h"
```

```bash
wget "https://richardogoma.pythonanywhere.com/data?currency=USD&timerange=1h"
```

```powershell
iwr "https://richardogoma.pythonanywhere.com/data?currency=USD&timerange=1h"
```
<img width="840" alt="Screenshot 2023-06-22 120529" src="https://github.com/richardogoma/bitcoin-rate-tracker/assets/121939700/03b5a173-376a-4c0a-a9cf-becd947abe33">

#### View Function: `querydata()`

The `querydata()` function is the view function associated with the `/data` endpoint. It handles the GET requests to this endpoint.

The function performs the following steps:

1. Validates the request method. If it's not a GET request, it returns a 400 (Bad Request) response.
2. Extracts the query parameters `currency` and `timerange` from the request.
3. Validates the query parameters using regular expressions (regex) patterns.
4. Extracts the validated parameters and prepares them for data retrieval.
5. Calls the `retrieve_bitcoin_data()` function from the `pre_processor` module to retrieve the Bitcoin rate data.
6. Constructs a JSON response with the retrieved data and returns it with a 200 (OK) status code.
7. If any errors occur during the process, appropriate error messages are returned with a 400 (Bad Request) or 500 (Internal Server Error) status code.

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