import urllib3
import json
import re
from elasticsearch import Elasticsearch
import warnings
from sqlalchemy.exc import SAWarning

from kph.src.config.config import config
from kph.src.ingest.mappings import doc_body, page_body

# Suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

warnings.filterwarnings("ignore", message=".*REGCONFIG().*", category=SAWarning)

# Suppress specific Elasticsearch warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# If you're getting SSL warnings and you understand the risks, you can suppress them too
warnings.filterwarnings("ignore", message="Unverified HTTPS request is being made")

sb = "\033[1m\033[96m"  # Start tag for bold and blue text
eb = "\033[0m"  # End tag to reset formatting


INDEX_DOCS_BASE_NAME = config.elasticsearch.indices.docs.base_name
INDEX_DOCS_ALIAS = config.elasticsearch.indices.docs.alias

INDEX_PAGES_BASE_NAME = config.elasticsearch.indices.pages.base_name
INDEX_PAGES_ALIAS = config.elasticsearch.indices.pages.alias

DOC_EMBEDDING_MODEL_ID = config.azure_openai_clients.text_embedding.model
DOC_EMBEDDING_MODEL_DIMENSION = (
    config.azure_openai_clients.text_embedding.dimension_docs
)

PAGE_EMBEDDING_MODEL_ID = config.azure_openai_clients.text_embedding.model
PAGE_EMBEDDING_MODEL_DIMENSION = (
    config.azure_openai_clients.text_embedding.dimension_pages
)

IMAGE_EMBEDDING_MODEL_ID = config.image_embedding.model
IMAGE_EMBEDDING_MODEL_DIMENSION = config.image_embedding.dimension

CREATE_NEW_INDEX = True

es = Elasticsearch(
    config.elasticsearch.host,
    http_auth=(config.elasticsearch.username, config.elasticsearch.password),
    verify_certs=False,
)


def get_or_create_index(es, index_base_name, index_alias, body):
    # Function to extract version numbers and find the next available version
    def get_next_index_version(base_name):
        try:
            # Get all indices that match the base name pattern
            all_indices = es.indices.get_alias(name="*", index=f"{base_name}-v*")
        except Exception as e:
            print(f"Error retrieving indices: {str(e)}")
            all_indices = {}

        # Compile a regex pattern to match indices with version numbers
        pattern = re.compile(rf"^{base_name}-v(\d{{3}})$")

        # Extract existing version numbers
        versions = [
            int(m.group(1))
            for index in all_indices
            for m in [pattern.match(index)]
            if m
        ]

        # Find the next version number
        next_version = max(versions) + 1 if versions else 1

        # Return the next version number in a 3-digit format
        return f"{base_name}-v{next_version:03d}"

    try:
        if CREATE_NEW_INDEX:
            index_name = get_next_index_version(index_base_name)

            # Delete existing indices with the alias (optional based on your requirements)
            if es.indices.exists_alias(name=index_alias):
                indices_to_delete = es.indices.get_alias(name=index_alias).keys()
                for idx in indices_to_delete:
                    es.indices.delete_alias(index=idx, name=index_alias)
                    es.indices.delete(index=idx)

            body["aliases"] = {index_alias: {}}

            # Create the index with the determined name
            es.indices.create(index=index_name, body=body)
            print(f"Created index '{index_name}' with alias '{index_alias}'")
        else:
            # Get the current index name using the alias, assuming alias exists and is unique
            index_name = list(es.indices.get_alias(name=index_alias).keys())[0]
            print(f"Using existing index '{index_name}' with alias '{index_alias}'")

        return index_name
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise


def ingest_document(document):

    file_metadata = {
        "file_directory": document["doc_file_metadata"].get(
            "file_directory", "not specified"
        ),
        "file_name": document["doc_file_metadata"].get("filename", "not specified"),
        "file_type": document["doc_file_metadata"].get("file_type", "not specified"),
        "last_modified": document["doc_file_metadata"].get(
            "last_modified", "not specified"
        ),
        "languages": document["doc_file_metadata"].get("languages", "not specified"),
        "slide_images_path": document["doc_file_metadata"].get(
            "slide_images_path", "not specified"
        ),
    }

    # Flatten doc_extracted_metadata
    metadata = {
        key.lower().replace(" ", "_"): value["value"]
        for key, value in document["doc_extracted_metadata"].items()
    }

    completion_year = metadata.get("completion_year")
    if completion_year == "not specified":
        completion_year = None  # Or assign a default value

    pocs_raw = document["doc_extracted_metadata"].get("pocs", {}).get("value")
    if not isinstance(pocs_raw, list):  # Ensuring 'pocs' is a list
        pocs = (
            []
        )  # Default to an empty list if 'pocs' is not properly formatted or unspecified
    else:
        # Format 'pocs' as per the Elasticsearch mapping
        pocs = [
            {
                "name": poc.get("name", "not specified"),
                "email": poc.get("email", "not specified"),
                "role": poc.get("role", "not specified"),
            }
            for poc in pocs_raw
        ]

    # Prepare metadata text
    full_metadata = {
        key.lower().replace(" ", "_"): value
        for key, value in document["doc_extracted_metadata"].items()
    }
    metadata_text = "\n".join(
        [f"{key}: {value}" for key, value in full_metadata.items()]
    )
    metadata_text = metadata_text.strip()

    # Prepare document for indexing
    doc_to_index = {
        "doc_id": document["doc_id"],
        "file_metadata": file_metadata,
        "document_type": metadata.get("document_type"),
        "title": metadata.get("title"),
        "author": metadata.get("author"),
        "agency_name": metadata.get("agency_name"),
        "client_name": metadata.get("client_name"),
        "project_name": metadata.get("project_name"),
        "pid": metadata.get("pid"),
        "url": metadata.get("url"),
        "referenceable": metadata.get("referenceable"),
        "pocs": pocs,
        "country": metadata.get("country"),
        "region": metadata.get("region"),
        "industry": metadata.get("industry"),
        "capabilities": metadata.get("capabilities"),
        "services": metadata.get("services"),
        "completion_year": completion_year,
        "budget_spend": metadata.get("budget_spend"),
        "key_technologies": metadata.get("key_technologies"),
        "partners_involved": metadata.get("partners_involved"),
        "keywords": metadata.get("keywords"),
        "confidentiality": metadata.get("confidentiality"),
        "problem": metadata.get("problem"),
        "imperative_for_change": metadata.get("imperative_for_change"),
        "solution": metadata.get("solution"),
        "impact": metadata.get("impact"),
        "long_summary": metadata.get("long_summary"),
        "short_summary": metadata.get("short_summary"),
        "doc_metadata_text": metadata_text,
        "doc_full_text": document.get("doc_text"),
        "doc_markdown_text": document.get("doc_markdown_text"),
        "doc_html_text": document.get("doc_html_text"),
        "doc_unstructured_text": document.get("doc_text_unstructured"),
        "doc_embedding": document.get(
            "embedding", [0] * DOC_EMBEDDING_MODEL_DIMENSION
        ),  # Adjust if embedding is always provided
    }

    # Index the document
    es.index(index=INDEX_DOCS_ALIAS, id=document["doc_id"], document=doc_to_index)

    # Prepare and index each page associated with the document
    for page in document["pages"]:
        page_to_index = {
            "doc_id": document["doc_id"],  # Reference to the parent document
            "page_id": page["page_id"],
            "page_no": page["page_no"],
            "page_text": page.get("text", ""),
            "page_markdown": page.get("markdown", ""),
            "page_html": page.get("html", ""),
            "text_unstructured": page.get("text_unstructured", ""),
            "page_image_path": page.get("image_path", ""),
            # Assuming pages might have embeddings similar to documents
            "page_embedding": page.get(
                "page_embedding", [0] * DOC_EMBEDDING_MODEL_DIMENSION
            ),  # Adjust accordingly
        }

        # Index the page into the 'pages' index
        es.index(index=INDEX_PAGES_ALIAS, id=page["page_id"], document=page_to_index)

    print(f"Document {document['doc_id']} and all its pages indexed.")


if __name__ == "__main__":

    INDEX_DOCS_NAME = get_or_create_index(
        es, INDEX_DOCS_BASE_NAME, INDEX_DOCS_ALIAS, doc_body
    )
    INDEX_PAGES_NAME = get_or_create_index(
        es, INDEX_PAGES_BASE_NAME, INDEX_PAGES_ALIAS, page_body
    )

    # Open full_jsons_with_embeddings
    with open(
        config.paths.postprocessed_embed_path,
        "r",
    ) as f:
        full_jsons_with_embeddings = json.load(f)

    if CREATE_NEW_INDEX:
        for document in full_jsons_with_embeddings:
            ingest_document(document)
