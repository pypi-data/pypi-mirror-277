import json
from kph.src.retrieval.elasticsearch_utils import (
    search_hybrid,
    search_with_filter_removal,
    count_docs_by_field_values,
    view_360,
)
from kph.src.retrieval.print_utils import print_logs
from kph.src.common.sample_queries import queries


if __name__ == "__main__":
    # query = "Find examples of work for automotive clients in the United States from no later than 2022"
    # query = "client_name:'Delta' services:'Strategy & Consulting' in the past 24 months"
    # # query = "file_name:'Chevron_Business Transformation Strategy MC Learning_Case Study_2019' client_name:Chevron"
    # query = "Provide an example of business transformation work for a global CPG client by ps or rzf or pdx in cx or dx or ux in na."
    # # query = "B2B FinServ/Bank cases from Digitas or RZF or PS in NA between 2020-22 in digital business transformaton."
    # # query = "service:'Digital Maturity'"
    # # query = "Rx Product"
    # # query = "Find case studies for banks in Southeast Asia only from 2022 or later."
    # # query = "Find case studies for customer experience work in the retail or telecom space in asia or europe between 2016 & 24"

    # res, logs = search_hybrid(query, rerank=True)
    # print_logs(logs)

    # variations_results = search_with_filter_removal(logs)
    # print(json.dumps(variations_results, indent=1))

    # # Assuming 'response' contains your previous response object
    # view_360_response = view_360()
    # aggregations_result = count_docs_by_field_values(
    #     view_360_response["aggregations"], logs["field_value_pairs"]
    # )
    # print(aggregations_result)

    import pandas as pd

    # Initialize an empty DataFrame
    df = pd.DataFrame(columns=["query", "kw_results", "knn_results", "final_results"])

    for i, query in enumerate(queries):
        print(f"Query: {query}")
        res, logs = search_hybrid(query)
        print_logs(logs)

        # Append the query and relevant fields from logs to the DataFrame
        df.loc[i] = [
            query,
            logs["kw_results"],
            logs["knn_results"],
            logs["final_results"],
        ]

    # Save df
    df.to_csv("outputs/logs/search_results.csv", index=False)
