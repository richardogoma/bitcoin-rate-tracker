#!/usr/bin/env python3
import requests
from config import Config


def retrieve_rates(uri: str) -> dict:
    response = requests.request("GET", uri, timeout=60)
    if response.status_code == 200:
        deserialized_response = response.json()
        return deserialized_response


def main():
    response = retrieve_rates(uri=Config.API_URI)
    print(f"Response of {type(response)} \n{response}")


if __name__ == "__main__":
    main()
