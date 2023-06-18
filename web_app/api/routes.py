"""Web application api routes and view functions"""

import re
from flask import Blueprint, jsonify, request, make_response
from src.data.pre_processor import retrieve_bitcoin_data

# Blueprint Configuration
api_bp = Blueprint(
    "api_bp", __name__, template_folder="templates", static_folder="static"
)


@api_bp.route("/data", methods=["GET"])
def querydata():
    """
    Route request based on query parameters to the endpoint.
    Expected query parameters: currency (3-letter code), timerange (in hours).
    """
    if request.method != "GET":
        return make_response("Malformed request", 400)

    # Extract query parameters
    currency = request.args.get("currency")
    timerange = request.args.get("timerange")

    # Define regex patterns for validation and extraction
    patterns = [
        (re.compile(r"^([a-zA-Z]{3})$"), currency),
        (re.compile(r"^([1-9]|[1-3][0-9]|4[0-8])h$"), timerange),
    ]

    params = [
        pattern.match(variable).group(1)
        for pattern, variable in patterns
        if pattern.match(variable)
    ]

    try:
        # Extract validated parameters
        rate_type = f"{params[0].lower()}_rate"
        minutes = int(params[1]) * 60

    except (IndexError, TypeError) as error_msg:
        return make_response(
            jsonify({"Bad Request": f"Provide valid query parameters, {error_msg}"}),
            400,
        )

    try:
        print(
            f"Retrieving Bitcoin {rate_type.replace('_', ' ')}s within {minutes} mins from the lastest data in database..."
        )
        data = retrieve_bitcoin_data(rate_type, time_range=(minutes,))

        if data is None:
            raise IOError("Failed to retrieve data from the database")

        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(data), 200, headers)

    except IOError as error_msg:
        return make_response(jsonify({"Internal Server Error": str(error_msg)}), 500)
