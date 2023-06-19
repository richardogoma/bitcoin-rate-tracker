"""Web application home routes and view functions"""

import requests
from flask import Blueprint, request, make_response, jsonify, render_template

# Blueprint Configuration
home_bp = Blueprint(
    "home_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/home/static",
)


@home_bp.route("/", methods=["GET"])
def home():
    """Homepage."""

    if request.method != "GET":
        return make_response("Malformed request", 400)

    try:
        # Extract query parameters
        currency = request.args.get("currency")
        if not currency:
            currency = "USD"

        url = f"http://127.0.0.1:5051/data?currency={currency}&timerange=48h"
        data = retrieve_rates(uri=url)

        print(f"Rendering Bitcoin {currency} prices at /index.html")
        return render_template(
            "index.html",
            data=data,
            title="Bitcoin Price Index Live Chart",
            currency_variable=currency,
        )

    except requests.exceptions.HTTPError as error_msg:
        return make_response(jsonify({"Internal Server Error": str(error_msg)}))


def retrieve_rates(uri: str) -> list:
    """
    Retrieve rates from the given URI.

    Args:
        uri (str): The URI to fetch the rates from.

    Returns:
        list: A list of rates.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the request.
        ValueError: If the response does not contain valid JSON data.

    """
    try:
        response = requests.get(uri, timeout=60)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as error_msg:
        print(f"An error occurred while making the request: {error_msg}")
        raise error_msg
    except ValueError as error_msg:
        print(f"Error: Invalid JSON data - {error_msg}")
        raise error_msg
