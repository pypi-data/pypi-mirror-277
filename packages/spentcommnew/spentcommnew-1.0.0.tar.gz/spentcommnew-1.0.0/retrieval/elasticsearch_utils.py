import logging
import time
import warnings
import urllib3
import re
import copy
from omegaconf import OmegaConf
from elasticsearch import Elasticsearch
from sqlalchemy.exc import SAWarning

from kph.src.config.config import config
from kph.src.common.embedding import get_embedding
from kph.src.retrieval.query_parsing import preprocess_query, parse_query_ner
from kph.src.retrieval.rerank import rerank_and_normalize_documents

# Suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

warnings.filterwarnings("ignore", message=".*REGCONFIG().*", category=SAWarning)

# Suppress specific Elasticsearch warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# If you're getting SSL warnings and you understand the risks, you can suppress them too
warnings.filterwarnings("ignore", message="Unverified HTTPS request is being made")

logger = logging.getLogger(__name__)


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


es = Elasticsearch(
    config.elasticsearch.host,
    http_auth=(config.elasticsearch.username, config.elasticsearch.password),
    verify_certs=False,
)

# Convert fields from OmegaConf to Python list
fields = OmegaConf.to_container(config.elasticsearch.fields, resolve=True)


def build_es_query(
    query,
    quoted_keywords,
    should_have_keywords,
    excluded_keywords,
    field_value_pairs,
    fields=fields,
    verbose=False,
):
    # Initialize the query structure
    bool_query = {
        "bool": {
            "must": [],
            "should": [],
            "must_not": [],
        }
    }

    # Handle single and quoted keywords
    for keyword in quoted_keywords:
        bool_query["bool"]["must"].append(
            {
                "match_phrase": {
                    "doc_unstructured_text": {
                        "query": keyword,
                        "slop": config.elasticsearch.slop,
                    }
                }
            }
        )
    for keyword in should_have_keywords:
        bool_query["bool"]["should"].append(
            {
                "match": {
                    "doc_unstructured_text": {
                        "query": keyword,
                        "operator": "and",
                        "fuzziness": "AUTO",
                    }
                }
            }
        )
    for keyword in excluded_keywords:
        bool_query["bool"]["must_not"].append(
            {"match": {"doc_unstructured_text": keyword}}
        )

    # Handle multiple values fields with 'should' clauses for agencies and other fields
    for field, terms in field_value_pairs.items():

        # # @TODO: Must be fixed in the query processing time
        # if field == 'industry' and 'Media & Technology' in field_value_pairs['industry']:
        #     # delete the 'Media & Technology' from the list
        #     field_value_pairs['industry'].remove('Media & Technology')

        if field in ("year", "file_name"):
            continue

        should_clauses = [
            {"match": {f"{field}.keyword": term}} for term in field_value_pairs[field]
        ]
        if should_clauses:
            bool_query["bool"]["must"].append(
                {
                    "bool": {
                        "should": should_clauses,
                        "minimum_should_match": config.elasticsearch.minimum_should_match,
                    }
                }
            )

    # Handle file_name
    if "file_name" in field_value_pairs:
        should_clauses = [
            {"match": {"file_metadata.file_name": term}}
            for term in field_value_pairs["file_name"]
        ]
        if should_clauses:
            bool_query["bool"]["must"].append(
                {
                    "bool": {
                        "should": should_clauses,
                        "minimum_should_match": config.elasticsearch.minimum_should_match,
                    }
                }
            )

    # Handle date ranges and exact year or multiple years
    if "year" in field_value_pairs:
        year_range = field_value_pairs["year"]
        if isinstance(year_range, dict):
            # Range condition
            if "gte" in year_range or "lte" in year_range:
                bool_query["bool"]["must"].append(
                    {
                        "range": {
                            "completion_year": {
                                "gte": year_range.get("gte", None),
                                "lte": year_range.get("lte", None),
                            }
                        }
                    }
                )
            # Multiple exact years condition
            elif "eq" in year_range:
                should_clauses = []
                for year in year_range["eq"]:
                    should_clauses.append(
                        {"range": {"completion_year": {"gte": year, "lte": year}}}
                    )
                if should_clauses:
                    bool_query["bool"]["must"].append(
                        {
                            "bool": {
                                "should": should_clauses,
                                "minimum_should_match": config.elasticsearch.minimum_should_match,
                            }
                        }
                    )

    # General query with multi_match
    if query.strip():
        bool_query["bool"]["must"].append(
            {
                "multi_match": {
                    "query": query,
                    "fields": fields,
                    "operator": "or",
                    "fuzziness": "AUTO",
                }
            }
        )

    if verbose:
        print(f"Constructed Elasticsearch Query: {bool_query}")

    return bool_query


def process_and_build_query(query):
    logging.basicConfig(level=logging.INFO)

    # Assume preprocess_query and parse_query_ner are functions that have been defined elsewhere
    (
        preprocessed_query,
        quoted_keywords,
        should_have_keywords,
        excluded_keywords,
        field_value_pairs,
    ) = preprocess_query(query)
    # Log all the extracted information
    # logging.info(
    #     f"Preprocessed Query: {preprocessed_query}\n Quoted Keywords: {quoted_keywords}\n Should Have Keywords: {should_have_keywords}\n Excluded Keywords: {excluded_keywords}\n Field Value Pairs: {field_value_pairs}"
    # )

    # Parse the query to extract named entities and other elements like capabilities and services
    entity_results = parse_query_ner(preprocessed_query)
    # logging.info(f"Entity Results: {json.dumps(entity_results, indent=4)}")

    # Add entity_results to field_value_pairs
    for key, value in entity_results.items():
        if key not in field_value_pairs:
            field_value_pairs[key] = value

    # Log the updated field_value_pairs
    # logging.info(f"Updated Field Value Pairs: {field_value_pairs}")

    # Build Elasticsearch query
    es_query = build_es_query(
        query=preprocessed_query,
        quoted_keywords=quoted_keywords,
        should_have_keywords=should_have_keywords,
        excluded_keywords=excluded_keywords,
        field_value_pairs=field_value_pairs,
        fields=fields,
        verbose=False,
    )

    return es_query, (
        preprocessed_query,
        quoted_keywords,
        should_have_keywords,
        excluded_keywords,
        field_value_pairs,
        entity_results,
    )


def extract_scores(es_results):
    """Extracts scores from Elasticsearch results into a dict format."""
    return {hit["_id"]: hit["_score"] for hit in es_results["hits"]["hits"]}


def normalize_scores(scores):
    """Normalizes scores to a 0-1 scale based on the maximum score."""
    if not scores:
        return {}
    max_score = max(scores.values())
    return {doc_id: score / max_score for doc_id, score in scores.items()}


def weighted_reciprocal_rank_fusion(
    es_results_kw, es_results_knn, weight_kw=1, weight_knn=1, verbose=False
):
    # Extract and normalize scores from each results set
    scores_kw = normalize_scores(extract_scores(es_results_kw))
    scores_knn = normalize_scores(extract_scores(es_results_knn))

    # Assuming extraction of `_source` data is feasible
    source_data = {
        hit["_id"]: hit.get("_source") for hit in es_results_kw["hits"]["hits"]
    }
    source_data.update(
        {hit["_id"]: hit.get("_source") for hit in es_results_knn["hits"]["hits"]}
    )

    # Combine normalized scores with weights
    combined_scores = {}
    for doc_id, score in scores_kw.items():
        combined_scores[doc_id] = combined_scores.get(doc_id, 0) + score * weight_kw
    for doc_id, score in scores_knn.items():
        combined_scores[doc_id] = combined_scores.get(doc_id, 0) + score * weight_knn

    # Normalize combined scores again
    max_combined_score = max(
        combined_scores.values(), default=1
    )  # Avoid division by zero
    normalized_combined_scores = {
        doc_id: score / max_combined_score for doc_id, score in combined_scores.items()
    }

    # Sort documents by normalized combined scores in descending order
    sorted_docs = sorted(
        normalized_combined_scores.items(), key=lambda x: x[1], reverse=True
    )

    # Adjust to include _source data
    search_results = {
        "hits": {
            "hits": [
                {"_id": doc_id, "_score": score, "_source": source_data.get(doc_id)}
                for doc_id, score in sorted_docs
            ]
        }
    }

    if verbose:
        print(f"Combined scores (normalized): {normalized_combined_scores}")

    return search_results


def search_hybrid(
    query,
    apply_advanced_filtering=True,
    k=5,
    es=es,
    index=INDEX_DOCS_ALIAS,
    source=[
        "file_metadata",
        "file_metadata.file_name",
        "client_name",
        "project_name",
        "agency_name",
        "industry",
        "region",
        "country",
        "completion_year",
        "capabilities",
        "services",
        "keywords",
        "key_technologies",
        "problem",
        "imperative_for_change",
        "impact",
        "solution",
        "short_summary",
        "long_summary",
        "doc_metadata_text",
    ],
    rerank=False,
    verbose=False,
):

    start_time = time.time()

    # Split the query into tokens based on spaces and ':' for field-value pairs
    query_tokens = re.split("[: ]+", query)
    query_len = len(query_tokens)

    es_query, (
        cleaned_query,
        quoted_keywords,
        should_have_keywords,
        excluded_keywords,
        field_value_pairs,
        entity_results,
    ) = process_and_build_query(query)

    if verbose:
        print(f"es_query: {es_query}")
        print(
            f"cleaned_query: {cleaned_query},\n quoted_keywords: {quoted_keywords},\n should_have_keywords: {should_have_keywords},\n excluded_keywords: {excluded_keywords},\n field_value_pairs: {field_value_pairs},\n entity_results: {entity_results}"
        )

    search_results_kw = es.search(
        index=index,
        query=es_query,
        source=source,
    )

    kw_results_ids = [hit["_id"] for hit in search_results_kw["hits"]["hits"]]
    kw_results = [
        (hit["_source"]["file_metadata"]["file_name"], hit["_score"])
        for hit in search_results_kw["hits"]["hits"]
    ]

    knn_results_ids, knn_results = [], []
    hybrid_results_before_reranking_ids, hybrid_results_before_reranking = [], []

    search_results = search_results_kw

    if (
        query_len == 1 or cleaned_query != query
    ):  # If the cleaned query is different from the original query, use the keyword search
        lexical_cues = True
        if apply_advanced_filtering:
            search_type = "keyword_search_with_advanced_filters"
            if query_len == 1:
                search_type_reason = (
                    "Single keyword query & apply_advanced_filtering = True"
                )
            else:
                search_type_reason = "Query changed (lexical cues in the query) & apply_advanced_filtering = True"
        else:
            if query_len == 1:
                search_type = "keyword_search"
                search_type_reason = (
                    "Single keyword query & apply_advanced_filtering = False"
                )
            else:
                search_type = "keyword_search"
                search_type_reason = "Query changed (lexical cues in the query) & apply_advanced_filtering = False"

    else:  # If the cleaned query is the same as the original query, use the hybrid search

        search_type = "hybrid"
        search_type_reason = "Query did not change (no lexical cues in the query) & apply_advanced_filtering = False"
        # Use kw_results_ids as filter for KNN search
        knn = (
            {
                "field": "doc_embedding",
                "query_vector": get_embedding(cleaned_query),
                "k": k * 2,
                "num_candidates": k * 5,
                "filter": {"terms": {"_id": kw_results_ids}},
            },
        )

        search_results_knn = es.search(
            index=index,
            knn=knn,
            size=k * 2,
            source=source,
        )

        knn_results_ids = [hit["_id"] for hit in search_results_knn["hits"]["hits"]]
        knn_results = [
            (hit["_source"]["file_metadata"]["file_name"], hit["_score"])
            for hit in search_results_knn["hits"]["hits"]
        ]

        # Combine the results from the keyword search and the KNN search by using weighted reciprocal rank fusion
        search_results = weighted_reciprocal_rank_fusion(
            es_results_kw=search_results_kw,
            es_results_knn=search_results_knn,
            weight_kw=config.elasticsearch.kw_weight,
            weight_knn=config.elasticsearch.knn_weight,
            verbose=verbose,
        )

    # Get the id and file name of the results
    hybrid_results_before_reranking_ids = [
        hit["_id"] for hit in search_results["hits"]["hits"]
    ]
    hybrid_results_before_reranking = [
        (hit["_source"]["file_metadata"]["file_name"], hit["_score"])
        for hit in search_results["hits"]["hits"]
    ]

    # Reranking
    if rerank:
        search_results = rerank_and_normalize_documents(query, search_results)

    search_results["hits"]["hits"] = search_results["hits"]["hits"][:k]

    # Now extracting IDs should be straightforward as the reranked results are already in the correct format
    final_results_ids = [hit["_id"] for hit in search_results["hits"]["hits"]]
    final_results = [
        (hit["_source"]["file_metadata"]["file_name"], hit["_score"])
        for hit in search_results["hits"]["hits"]
    ]

    # Stop the timer and calculate the duration
    end_time = time.time()
    processing_time = round(end_time - start_time, 1)

    if verbose:
        # Print processing time
        print(f"\n{sb}Processing time:{eb} {processing_time:.2f} seconds")
        print("*" * 100, "\n\n")

    # Get long summary of the top 3 results
    top_results = search_results["hits"]["hits"][:3]
    top_summaries = [
        hit["_source"].get("short_summary", "Summary not available")
        for hit in top_results
    ]

    logs = {
        "query": query,
        "apply_advanced_filtering": apply_advanced_filtering,
        "identified_entities": entity_results,
        "cleaned_query": cleaned_query,
        "quoted_keywords": quoted_keywords,
        "should_have_keywords": should_have_keywords,
        "excluded_keywords": excluded_keywords,
        "field_value_pairs": field_value_pairs,
        "number_of_results_after_filters": search_results_kw["hits"]["total"]["value"],
        "elastic_query": es_query,
        "search_type": search_type,
        "search_type_reason": search_type_reason,
        "kw_results_ids": kw_results_ids,
        "kw_results": kw_results,
        "knn_results_ids": knn_results_ids,
        "knn_results": knn_results,
        "hybrid_results_before_reranking_ids": hybrid_results_before_reranking_ids,
        "hybrid_results_before_reranking": hybrid_results_before_reranking,
        "final_results_ids": final_results_ids,
        "final_results": final_results,
        "top_summaries": top_summaries,
        "processing_time": processing_time,
    }

    return search_results, logs


def perform_es_search(
    query,
    es=es,
    index=INDEX_DOCS_ALIAS,
    source=[
        "file_metadata.file_name",
        "client_name",
        "agency_name",
        "industry",
        "region",
        "country",
        "completion_year",
        "capabilities",
        "services",
        "short_summary",
    ],
):
    try:
        # print("Executing query:")
        # print(json.dumps(query, indent=4))  # Print the query to visually inspect its structure
        response = es.search(
            index=index,
            query=query,
            source=source,
            size=config.elasticsearch.max_results,
        )
        return response
    except Exception as e:
        print("Error performing search:", str(e))
        return []



def search_with_filter_removal(logs):

    query = logs["query"]
    cleaned_query = logs["cleaned_query"]
    quoted_keywords = logs["quoted_keywords"]
    should_have_keywords = logs["should_have_keywords"]
    excluded_keywords = logs["excluded_keywords"]
    field_value_pairs = logs["field_value_pairs"]

    start_time = time.time()  # Start timing here

    results_dict = {}

    if quoted_keywords:
        results_dict["quotes_removed"] = perform_condition_search(
            query=cleaned_query,
            quoted_keywords=[],
            should_have_keywords=should_have_keywords,
            excluded_keywords=excluded_keywords,
            field_value_pairs=field_value_pairs,
            field=None,
            condition=f"quotes_removed: {quoted_keywords}",
        )

    # Iterate through each field in field_value_pairs
    for field in list(field_value_pairs.keys()):
        original_conditions = field_value_pairs[field]

        if not original_conditions:  # Skip empty field condition lists
            continue

        # Remove the entire field and perform the search
        modified_field_value_pairs = copy.deepcopy(field_value_pairs)
        modified_field_value_pairs.pop(field, None)
        results_dict[field] = perform_condition_search(
            query=cleaned_query,
            quoted_keywords=quoted_keywords,
            should_have_keywords=should_have_keywords,
            excluded_keywords=excluded_keywords,
            field_value_pairs=modified_field_value_pairs,
            field=field,
            condition=f"{field}: {original_conditions}",
        )

        # Perform search with each condition removed one by one, only if more than one condition exists
        if len(original_conditions) > 1:
            for condition in original_conditions:
                modified_field_value_pairs = copy.deepcopy(field_value_pairs)
                # Remove just the current condition from the field
                modified_field_value_pairs[field] = [
                    item
                    for item in modified_field_value_pairs[field]
                    if item != condition
                ]

                if not modified_field_value_pairs[
                    field
                ]:  # If the list is empty after removal, pop the field
                    modified_field_value_pairs.pop(field, None)

                search_condition_removed = f"{field}: {condition}"
                # Build and perform search for each condition removed
                condition_key = f"{field} - removed {condition}"
                results_dict[condition_key] = perform_condition_search(
                    query=cleaned_query,
                    quoted_keywords=quoted_keywords,
                    should_have_keywords=should_have_keywords,
                    excluded_keywords=excluded_keywords,
                    field_value_pairs=modified_field_value_pairs,
                    field=field,
                    condition=search_condition_removed,
                )

    # Capture end time after the function execution completes
    end_time = time.time()
    execution_time = end_time - start_time  # Calculate total execution time
    results_dict["execution_time_seconds"] = execution_time

    return results_dict


def perform_condition_search(
    query,
    quoted_keywords,
    should_have_keywords,
    excluded_keywords,
    field_value_pairs,
    field,
    condition,
):
    es_query = build_es_query(
        query=query,
        quoted_keywords=quoted_keywords,
        should_have_keywords=should_have_keywords,
        excluded_keywords=excluded_keywords,
        field_value_pairs=field_value_pairs,
        verbose=False,
    )

    search_results = perform_es_search(es_query)

    # Check for proper response structure
    if "hits" in search_results and "hits" in search_results["hits"]:
        return {
            "search_condition_removed": condition,
            "count of results after removal of the condition": search_results["hits"][
                "total"
            ].get("value", 0),
            "doc_ids": [hit["_id"] for hit in search_results["hits"]["hits"]],
        }
    else:
        print(
            f"Unexpected search results format or empty results for condition '{condition}' in field '{field}'"
        )
        return {
            "search_condition_removed": condition,
            "count of results after removal of the condition": 0,
        }


def view_360():
    # Define the aggregation query
    query_360 = {
        "size": 0,
        "aggs": {
            "agency_name": {
                "terms": {
                    "field": "agency_name.keyword",
                    "size": 100,  # Requesting up to 100 results, will display only top 10
                }
            },
            "client_name": {
                "terms": {
                    "field": "client_name.keyword",
                    "size": 10000,  # Requesting many results, but will only display top 10
                }
            },
            "country": {
                "terms": {
                    "field": "country.keyword",
                    "size": 300,  # Adjust based on the expected cardinality
                }
            },
            "region": {
                "terms": {
                    "field": "region.keyword",
                    "size": 10,  # Already fits the display limit
                }
            },
            "industry": {
                "terms": {
                    "field": "industry.keyword",
                    "size": 10,  # Already fits the display limit
                }
            },
            "capabilities": {
                "terms": {
                    "field": "capabilities.keyword",
                    "size": 50,  # Requesting many, displaying fewer
                }
            },
            "services": {
                "terms": {
                    "field": "services.keyword",
                    "size": 100,  # Requesting many, displaying fewer
                }
            },
            "key_technologies": {
                "terms": {
                    "field": "key_technologies.keyword",
                    "size": 100,  # Requesting up to 100 results, will display only top 10
                }
            },
            "partners_involved": {
                "terms": {
                    "field": "partners_involved.keyword",
                    "size": 50,  # Requesting many, displaying fewer
                }
            },
            "year": {
                "histogram": {
                    "field": "completion_year",
                    "interval": 1,
                }
            },
        },
    }

    def fix_year_data_in_response(response):
        if "aggregations" in response and "year" in response["aggregations"]:
            # Extract the year buckets from the original response
            original_buckets = response["aggregations"]["year"]["buckets"]
            fixed_buckets = []

            # Process each bucket to adjust the year key
            for bucket in original_buckets:
                # Convert the float key to an integer
                fixed_bucket = {
                    "key": int(bucket["key"]),  # Ensuring conversion for all cases
                    "doc_count": bucket["doc_count"],
                }
                fixed_buckets.append(fixed_bucket)

            # Update the original response object with fixed year buckets
            response["aggregations"]["year"]["buckets"] = fixed_buckets

        return response

    # Execute the search query
    response_360 = es.search(
        index=INDEX_DOCS_ALIAS, body=query_360
    )  # Replace "your_index_name" with your actual index name

    response_360 = fix_year_data_in_response(response_360)

    return response_360


def count_docs_by_field_values(aggregations, field_value_pairs):
    results = {}

    # Loop through each field specified in the input dictionary
    for field, values in field_value_pairs.items():

        # Initialize the result dictionary for this field
        results[field] = {}

        # Check if the correct aggregation key exists
        if (
            field in aggregations
            and "buckets" in aggregations[field]
            and field_value_pairs[field]
        ):
            buckets = aggregations[field]["buckets"]

            if field == "year" and isinstance(values, dict):
                # Compute the year range or exact matches from the filter parameters
                year_conditions = set()  # To store all valid years based on conditions

                if "eq" in values:
                    # Extend set with exact year matches if 'eq' is a list; otherwise add single value
                    year_conditions.update(
                        values["eq"]
                        if isinstance(values["eq"], list)
                        else [values["eq"]]
                    )

                if (
                    "gte" in values
                    or "lte" in values
                    or "gt" in values
                    or "lt" in values
                ):
                    min_year = min(
                        bucket["key"] for bucket in buckets
                    )  # Set to smallest year in buckets if not bounded below
                    max_year = max(
                        bucket["key"] for bucket in buckets
                    )  # Set to largest year in buckets if not bounded above

                    if "gt" in values:
                        min_year = max(min_year, values["gt"] + 1)
                    if "gte" in values:
                        min_year = max(min_year, values["gte"])
                    if "lt" in values:
                        max_year = min(max_year, values["lt"] - 1)
                    if "lte" in values:
                        max_year = min(max_year, values["lte"])

                    # Add range to set
                    year_conditions.update(range(min_year, max_year + 1))

                # Filter the buckets based on the computed set of valid years
                filtered_buckets = [
                    bucket
                    for bucket in buckets
                    if int(bucket["key"]) in year_conditions
                ]

                # Store results
                for bucket in filtered_buckets:
                    results[field][int(bucket["key"])] = bucket["doc_count"]

            else:
                # General handling for other fields
                filtered_buckets = [
                    bucket
                    for bucket in buckets
                    if not values or bucket["key"] in values
                ]

                # Store results
                for bucket in filtered_buckets:
                    results[field][bucket["key"]] = bucket["doc_count"]

    return results
