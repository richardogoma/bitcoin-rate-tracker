"""Web application home routes and view functions"""

import re
from flask import Blueprint, request, make_response, jsonify, render_template

# Blueprint Configuration
home_bp = Blueprint(
    "home_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/home/static",
)


@home_bp.route("/", methods=["GET", "HEAD"])
def home():
    """Homepage."""

    if request.method not in ["GET", "HEAD"]:
        return make_response("Malformed request", 400)

    # Extract query parameters
    currency = request.args.get("currency")
    if not currency:
        currency = "USD"

    # Define regex patterns for validation and extraction
    try:
        pattern = r"^(USD|EUR|GBP)$"
        match = re.match(pattern, currency)

        if not match:
            raise ValueError("Provide valid query parameters")

        currency = match.group(1).upper()

        print(f"Rendering Bitcoin {currency} prices at /index.html")
        return render_template(
            "index.html",
            title="Bitcoin Price Index Live Chart",
            currency_variable=f"{currency}",
        )

    except ValueError as error_msg:
        return make_response(
            jsonify({"Bad Request": f"{error_msg}"}),
            400,
        )
