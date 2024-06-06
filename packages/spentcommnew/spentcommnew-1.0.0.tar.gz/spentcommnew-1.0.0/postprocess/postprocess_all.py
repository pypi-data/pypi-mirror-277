# Read all json files in /home/jupyter/code/knowledge-powerhouse-pocs/notebooks/processing-staging/vault_pptx
import os
import json
import logging
import re
import argparse
from tqdm import tqdm  # Import tqdm for progress bar functionality
from pathlib import Path
from kph.src.config.config import config
from kph.src.postprocess.postprocess import postprocess
from kph.src.common.embedding import get_embedding

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Set the logging level to INFO

# Create a file handler that logs messages without time and INFO level
file_handler = logging.FileHandler("processing.log")
file_format = logging.Formatter("%(message)s")  # Define format without time and level
file_handler.setFormatter(file_format)

# Create a stream handler (console) with the default format including time and level
stream_handler = logging.StreamHandler()
stream_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(stream_format)

# Add both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def format_metadata(metadata, excluded_keys):
    formatted_text = []
    for key, value in metadata.items():
        if key not in excluded_keys:
            if isinstance(value, dict) and "value" in value:
                if value["value"] != "not specified":
                    formatted_text.append(f"{key}: {value['value']} \n")
            elif isinstance(value, list):
                formatted_text.append(f"{key}: {', '.join([str(v) for v in value])}")
    return " ".join(formatted_text)


def postprocess_all(
    summaries_path, postprocessed_path, postprocessed_embed_path, embed
):

    json_files = [
        pos_json
        for pos_json in os.listdir(summaries_path)
        if pos_json.endswith(".json")
        and not pos_json.startswith("!poc-docs-all-summaries-fulltext")
    ]

    full_jsons = []
    # Read the relevant text files for each json file and add the text to the json object
    for json_file in json_files:
        logger.info(f"\n\nProcessing {json_file}")
        # Use Path.stem to handle filenames with periods correctly
        filename = Path(json_file).stem
        # If the filenames have a double extension (.pptx.json), apply Path.stem again
        filename = Path(filename).stem
        with open(os.path.join(summaries_path, json_file), "r") as f:

            doc = json.load(f)
            # Post-process the json object
            doc = postprocess(doc)
            full_jsons.append(doc)

    # Save the full jsons to a file
    with open(postprocessed_path, "w") as f:
        json.dump(full_jsons, f, indent=6)

    logger.info(f"Saved postprocessed jsons to {postprocessed_path}")

    if not embed:
        logger.info("Embedding is disabled")
        return

    # Exclude specific keys
    excluded_keys_format = ["pocs", "url", "pid", "referenceable", "confidentiality"]

    full_jsons_with_embeddings = []

    # Use tqdm to show a progress bar for the outer loop
    for i, item in tqdm(enumerate(full_jsons), total=len(full_jsons)):
        for page in item["pages"]:
            text = page["text_unstructured"]
            # If wordcount of the text is less than a threshold, skip embedding
            if (
                len(text.split())
                < config.postprocessing_behavior.min_text_words_to_embed
            ):
                page["page_embedding"] = None
            else:
                page["page_embedding"] = get_embedding(
                    text,
                    model=config.azure_openai_clients.text_embedding.model,
                    dimension=config.azure_openai_clients.text_embedding.dimension_pages,
                )

        metadata = item["doc_extracted_metadata"]
        metadata_text = format_metadata(metadata, excluded_keys_format)

        embedding = get_embedding(
            metadata_text,
            model=config.azure_openai_clients.text_embedding.model,
            dimension=config.azure_openai_clients.text_embedding.dimension_docs,
        )
        item["metadata_text"] = metadata_text
        item["embedding"] = embedding
        full_jsons_with_embeddings.append(item)

    # Save full_jsons_with_embeddings
    with open(postprocessed_embed_path, "w") as f:
        json.dump(full_jsons_with_embeddings, f, indent=6)

    logger.info(
        f"Saved postprocessed jsons with embeddings to {postprocessed_embed_path}"
    )


if __name__ == "__main__":

    if not config.postprocessing_behavior.postprocess:
        logger.info("Postprocessing is disabled")
        exit()

    parser = argparse.ArgumentParser(description="Process documents for case studies")

    parser.add_argument(
        "--summaries_path",
        default=config.paths.summaries_path,
        help="Directory where the summaries are stored",
    )
    parser.add_argument(
        "--postprocessed_path",
        default=config.paths.postprocessed_path,
        help="Path to save the postprocessed json files",
    )
    parser.add_argument(
        "--embed",
        action="store_true",
        default=config.postprocessing_behavior.embed,
        help="Whether to embed or not",
    )
    parser.add_argument(
        "--postprocessed_embed_path",
        default=config.paths.postprocessed_embed_path,
        help="Path to save the postprocessed json files with embeddings",
    )

    args = parser.parse_args()

    postprocess_all(
        summaries_path=config.paths.summaries_path,
        postprocessed_path=args.postprocessed_path,
        postprocessed_embed_path=args.postprocessed_embed_path,
        embed=args.embed,
    )
