from kph.src.config.config import config

doc_body = {
    "settings": {
        # Include any custom settings here (e.g., number of shards, replicas)
    },
    "mappings": {
        "properties": {
            "doc_id": {"type": "keyword"},
            "file_metadata": {
                "type": "object",
                "properties": {
                    "file_directory": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword"}},
                    },
                    "file_name": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword"}},
                    },
                    "file_type": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword"}},
                    },
                    "last_modified": {
                        "type": "date",
                        "format": "strict_date_optional_time||epoch_millis",
                    },
                    "languages": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword"}},
                    },
                    "slide_images_path": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword"}},
                    },
                },
            },
            "document_type": {"type": "keyword"},
            "title": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "agency_name": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "client_name": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "project_name": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword"}},
            },
            "pid": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "url": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "author": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "referenceable": {"type": "keyword"},
            "confidentiality": {"type": "keyword"},
            "pocs": {
                "type": "nested",
                "properties": {
                    "source": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword"}},
                    },
                    "value": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "text",
                                "fields": {"keyword": {"type": "keyword"}},
                            },
                            "email": {
                                "type": "text",
                                "fields": {"keyword": {"type": "keyword"}},
                            },
                            "role": {
                                "type": "text",
                                "fields": {"keyword": {"type": "keyword"}},
                            },
                        },
                    },
                },
            },
            "country": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "region": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "industry": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "capabilities": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword"}},
            },
            "services": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "completion_year": {"type": "integer"},
            "budget_spend": {"type": "text"},
            "key_technologies": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword"}},
            },
            "partners_involved": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword"}},
            },
            "keywords": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "problem": {"type": "text"},
            "imperative_for_change": {"type": "text"},
            "solution": {"type": "text"},
            "impact": {"type": "text"},
            "long_summary": {"type": "text"},
            "short_summary": {"type": "text"},
            "doc_metadata_text": {"type": "text"},
            "doc_full_text": {"type": "text"},
            "doc_markdown_text": {"type": "text"},
            "doc_html_text": {"type": "text"},
            "doc_unstructured_text": {"type": "text"},
            "doc_embedding": {
                "type": "dense_vector",
                "dims": config.azure_openai_clients.text_embedding.dimension_docs,
                "similarity": config.elasticsearch.similarity,
                "element_type": "float",
                "index_options": {
                    "type": config.elasticsearch.index_options.type,
                    "m": config.elasticsearch.index_options.m,
                    "ef_construction": config.elasticsearch.index_options.ef_construction,
                },
                "meta": {
                    "model": config.azure_openai_clients.text_embedding.model,
                    "dimensions": str(
                        config.azure_openai_clients.text_embedding.dimension_docs
                    ),
                },
            },
        },
        "_source": {
            "excludes": [
                "doc_embedding",
            ]
        },
    },
}


page_body = {
    "settings": {
        # Include any custom settings here (e.g., number of shards, replicas)
    },
    "mappings": {
        "properties": {
            "doc_id": {"type": "keyword"},
            "page_id": {"type": "keyword"},
            "page_no": {"type": "integer"},
            "page_text": {"type": "text"},
            "page_markdown": {"type": "text"},
            "page_html": {"type": "text"},
            "text_unstructured": {"type": "text"},
            "page_image_path": {"type": "keyword"},
            "page_embedding": {
                "type": "dense_vector",
                "similarity": config.elasticsearch.similarity,
                "element_type": "float",
                "index_options": {
                    "type": config.elasticsearch.index_options.type,
                    "m": config.elasticsearch.index_options.m,
                    "ef_construction": config.elasticsearch.index_options.ef_construction,
                },
                "meta": {
                    "model": config.azure_openai_clients.text_embedding.model,
                    "dimensions": str(
                        config.azure_openai_clients.text_embedding.dimension_pages
                    ),
                },
            },
            "page_image_embedding": {
                "type": "dense_vector",
                "dims": config.image_embedding.dimension,
                "index": True,
                "similarity": config.elasticsearch.similarity,
                "element_type": "float",
                "index_options": {
                    "type": config.elasticsearch.index_options.type,
                    "m": config.elasticsearch.index_options.m,
                    "ef_construction": config.elasticsearch.index_options.ef_construction,
                },
                "meta": {
                    "model": config.image_embedding.model,
                    "dimensions": str(config.image_embedding.dimension),
                },
            },
        },
        "_source": {"excludes": ["page_embedding", "page_image_embedding"]},
    },
}
