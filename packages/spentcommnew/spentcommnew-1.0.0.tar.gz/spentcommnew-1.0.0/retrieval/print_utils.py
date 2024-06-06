import json
import logging

# Configure logging
logging.basicConfig(
    filename="outputs/logs/search_logs.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def print_logs(logs, indent=0):
    """
    A utility function named `print_logs` to log the `logs` dictionary in a nicely formatted way,
    preserving the order of fields and the ordering of 'ner_dict'.
    This version adds numbers to list elements for easier reference and ensures empty lists are printed as [].
    """
    logging.info(
        " ####################################### Search Logs ####################################### "
    )

    prefix = "  " * indent
    for key, value in logs.items():
        if "_ids" in key.lower():
            continue

        if isinstance(value, dict):
            logging.info(f"{prefix}{key}:")
            logging.info(json.dumps(value, indent=4))
        elif isinstance(value, list):
            if not value:
                logging.info(f"{prefix}{key}: []")
            else:
                logging.info(f"{prefix}{key}: [")
                for index, item in enumerate(value, start=1):
                    if isinstance(item, dict):
                        logging.info(f"{prefix}  {index}- {json.dumps(item, indent=4)}")
                    else:
                        logging.info(f"{prefix}  {index}- {item}")
                logging.info(f"{prefix}]")
        else:
            logging.info(f"{prefix}{key}: {value}")


def print_helper(search_results_knn, k):
    for i, hit in enumerate(search_results_knn["hits"]["hits"][:k], start=1):
        logging.info(f"{i}- {(hit['_source'], hit['_score'])}")


def pretty_print_results(results):
    logging.info("Results:")
    results = results["hits"]["hits"]
    for i, result in enumerate(results, start=1):
        document = result["_source"]
        logging.info(f"Result {i}:")
        logging.info(
            f"  File: {document.get('file_metadata', {}).get('file_name', 'Not specified')}"
        )
        logging.info(f"  Client Name: {document.get('client_name', 'Not specified')}")
        logging.info(f"  Project Name: {document.get('project_name', 'Not specified')}")
        logging.info(f"  Agency Name: {document.get('agency_name', 'Not specified')}")
        logging.info(f"  Country: {document.get('country', 'Not specified')}")
        logging.info(f"  Region: {document.get('region', 'Not specified')}")
        logging.info(f"  Industry: {document.get('industry', 'Not specified')}")
        logging.info(
            f"  Completion Year: {document.get('completion_year', 'Not specified')}"
        )
        logging.info(f"  Capabilities: {document.get('capabilities', 'Not specified')}")
        logging.info(f"  Services: {document.get('services', 'Not specified')}")
        logging.info(
            f"  Key Technologies: {document.get('key_technologies', 'Not specified')}"
        )
        logging.info(
            f"  Short Summary: {document.get('short_summary', 'Not specified')}"
        )
        logging.info("-" * 100)
