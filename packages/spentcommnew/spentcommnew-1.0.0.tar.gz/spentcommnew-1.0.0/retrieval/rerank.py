import requests
import logging

from kph.src.config.config import config

logger = logging.getLogger(__name__)


def rerank_documents(query, es_results):
    # logger.info(f"Reranking documents based on query: {query}")

    # Extract the 'long_summary' and map them to their respective Elasticsearch hit objects
    hits = es_results["hits"]["hits"]
    doc_id_to_summary = {
        hit["_id"]: hit["_source"]["long_summary"]
        for hit in hits
        if "long_summary" in hit["_source"]
    }
    summary_to_hit = {v: k for k, v in doc_id_to_summary.items()}
    docs_list = list(doc_id_to_summary.values())
    instances = [query] + docs_list
    payload = {"instances": instances}
    logger.debug(f"Instances sent for reranking: {payload}")

    # API call to reranking service
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            response = requests.post(config.reranker.api_url, json=payload)
            response.raise_for_status()
            reranked_data = response.json()["predictions"]
            logger.debug(f"API response status: {response.status_code}")
            logger.debug(f"Reranked data received: {reranked_data}")

            # Update the scores in the original hits based on reranked summaries
            for reranked in reranked_data:
                summary = reranked["passage"]
                new_score = reranked["score"]
                if summary in summary_to_hit:
                    doc_id = summary_to_hit[summary]
                    for hit in hits:
                        if hit["_id"] == doc_id:
                            init_score = hit["_score"]
                            hit["_score"] = new_score
                            logger.debug(
                                f"Updated score for document {doc_id}: {init_score} to {new_score}"
                            )

            # Sort the hits by the updated scores in descending order
            hits.sort(key=lambda x: x["_score"], reverse=True)

            # Prepare the reranked search results
            reranked_es_results = {"hits": {"total": len(hits), "hits": hits}}

            # print("Reranking completed and hits reordered based on new scores.")
            return reranked_es_results

        except requests.RequestException as e:
            attempts += 1
            logger.error(f"Reranking attempt {attempts} failed: {e}")
            if attempts == max_attempts:
                logger.error(
                    "Maximum retry attempts reached for reranking. Returning original results."
                )

    # Return the original results if all attempts fail
    return es_results


def rerank_and_normalize_documents(query, es_results):
    # Nested function for normalization
    def normalize_scores(scores):
        if not scores:
            return {}
        max_score = max(scores.values())
        min_score = min(scores.values())
        if max_score == min_score:
            return {doc_id: 0.75 for doc_id in scores}  # Midpoint of 0.6 and 0.9
        score_range = max_score - min_score
        base_normalized = {
            doc_id: (score - min_score) / score_range
            for doc_id, score in scores.items()
        }
        return {doc_id: 0.6 + 0.3 * score for doc_id, score in base_normalized.items()}

    # Rerank documents
    reranked_es_results = rerank_documents(query, es_results)
    hits = reranked_es_results["hits"]["hits"]

    # Extract scores and document IDs
    scores = {hit["_id"]: hit["_score"] for hit in hits}

    # Normalize the scores
    normalized_scores = normalize_scores(scores)
    # print(f"Normalized Scores: {normalized_scores}")

    # Update the hits with normalized scores
    for hit in hits:
        if hit["_id"] in normalized_scores:
            hit["_score"] = normalized_scores[hit["_id"]]

    # Sort the hits by the updated normalized scores in descending order
    hits.sort(key=lambda x: x["_score"], reverse=True)

    return {"hits": {"total": len(hits), "hits": hits}}
