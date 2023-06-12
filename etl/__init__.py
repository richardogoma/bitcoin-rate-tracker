from etl.extract.retriever import retrieve_rates
from etl.transform.parser import parse_dict


def start_etl(config):
    response = retrieve_rates(uri=config.API_URI)
    print(f"Response of {type(response)} \n{response}")

    parsed_data = parse_dict(response)
    print(f"Response of {type(parsed_data)} \n{parsed_data}")
