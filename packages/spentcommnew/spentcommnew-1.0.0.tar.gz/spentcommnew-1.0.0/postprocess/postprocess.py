import re
from fuzzywuzzy import fuzz
import fitz  # PyMuPDF

from kph.src.common.taxonomy import (
    agencies_dict,
    regions_dict,
    partners_involved_dict,
    industries_dict,
    acronym_to_full_names_dict,
    synonyms,
    capabilities_services_dict,
    countries_dict,
)
from kph.src.config.config import config


def normalize_not_specified(doc):
    if isinstance(doc, dict):
        return {k: normalize_not_specified(v) for k, v in doc.items()}
    elif isinstance(doc, list):
        return [normalize_not_specified(item) for item in doc]
    elif isinstance(doc, str):
        # Replace empty strings with "not specified"
        if doc == "":
            print("Replacing empty string with 'not specified'")
            return "not specified"
    return doc


def normalize_doc_type(doc):
    """
    Updates the document type if the client_name value is a list with more than one client and logs the changes.

    The function retrieves the file name from the data dictionary for logging purposes.
    """
    # Retrieve the file name from the data dictionary
    file_name = doc.get("doc_file_metadata", {}).get("filename", "Unknown file")

    client_name_value = (
        doc["doc_extracted_metadata"].get("client_name", {}).get("value", "")
    )

    # Check if client_name's value is a list with more than one item
    if isinstance(client_name_value, list) and len(client_name_value) > 1:
        # Update document_type to "Capability Deck"
        if (
            "document_type" in doc["doc_extracted_metadata"]
            and doc["doc_extracted_metadata"]["document_type"]["value"]
            != "Capability Deck"
        ):
            document_type_original_value = doc["doc_extracted_metadata"][
                "document_type"
            ]["value"]
            doc["doc_extracted_metadata"]["document_type"]["value"] = "Capability Deck"
            print(
                f"[{file_name}] Document type changed from '{document_type_original_value}' to 'Capability Deck'"
            )

            industry_original_value = doc["doc_extracted_metadata"]["industry"]["value"]
            doc["doc_extracted_metadata"]["industry"]["value"] = "not specified"
            print(
                f"[{file_name}] Industry changed from '{industry_original_value}' to 'not specified' as the client_name value is a list with more than one client."
            )

    return doc


def normalize_year(doc):
    completion_year = (
        doc["doc_extracted_metadata"].get("completion_year", {}).get("value", "")
    )
    if isinstance(completion_year, int) and completion_year >= 2015:
        return doc
    else:
        # doc['doc_extracted_metadata']['completion_year']['value'] = 2015
        file_name = doc.get("doc_file_metadata", {}).get("filename", "Unknown file")
        # See if we can find the year in the file name

        match = re.search(r"\b(20\d{2})\b", file_name)
        if match:
            year = int(match.group(1))
            doc["doc_extracted_metadata"]["completion_year"]["value"] = year
            doc["doc_extracted_metadata"]["completion_year"][
                "source"
            ] = f"Completion year updated from {completion_year} to {year} based on the file name."
            print(
                f"[{file_name}] Completion year updated from {completion_year} to {year} based on the file name."
            )

    return doc


def normalize_agency(
    agency_value, match_threshold=config.fuzzy_matching.agency_threshold
):
    """
    Normalize the agency value in the document.

    The function retrieves the file name from the data dictionary for logging purposes.
    """
    if agency_value:

        for agency, keywords in agencies_dict.items():
            for keyword in keywords:
                # Match against the service keywords
                score = fuzz.token_sort_ratio(keyword.lower(), agency_value.lower())
                if score >= match_threshold:
                    print(f"{agency_value} matched to {agency} with score {score}")
                    return agency

    return "not specified"


def normalize_region(
    region_value, match_threshold=config.fuzzy_matching.region_threshold
):
    """
    Normalize the region value in the document.

    The function retrieves the file name from the data dictionary for logging purposes.
    """
    if region_value:

        for region, keywords in regions_dict.items():
            for keyword in keywords:
                # Match against the service keywords
                score = fuzz.token_sort_ratio(keyword.lower(), region_value.lower())
                if score >= match_threshold:
                    print(f"{region_value} matched to {region} with score {score}")
                    return region

    return "not specified"


def normalize_country(
    country_value, match_threshold=config.fuzzy_matching.country_threshold
):
    """
    Normalize the country value in the document.

    The function retrieves the file name from the data dictionary for logging purposes.
    """
    if country_value:

        for country, keywords in countries_dict.items():
            for keyword in keywords:
                # Match against the service keywords
                score = fuzz.token_sort_ratio(keyword.lower(), country_value.lower())
                if score >= match_threshold:
                    print(f"{country_value} matched to {country} with score {score}")
                    return country

    return "not specified"


def normalize_industry(
    industry_value, match_threshold=config.fuzzy_matching.industry_threshold
):
    """
    Normalize the industry value in the document.

    The function retrieves the file name from the data dictionary for logging purposes.
    """
    if industry_value:

        for industry, keywords in industries_dict.items():
            for keyword in keywords:
                # Match against the service keywords
                score = fuzz.token_sort_ratio(keyword.lower(), industry_value.lower())
                if score >= match_threshold:
                    print(f"{industry_value} matched to {industry} with score {score}")
                    return industry

    return "not specified"


def extract_links_from_pdf(pdf_path, patterns):
    # Open the provided PDF file
    document = fitz.open(pdf_path)

    links = []

    # Convert simplified patterns to regular expressions
    regex_patterns = []
    for pattern in patterns:
        pattern = pattern.replace(".", r"\.")  # Escape dots
        pattern = pattern.replace("*", r".*")  # Replace * with .*
        regex_patterns.append(re.compile(pattern + r"/.*"))  # Ensure it ends with '/'

    # Iterate through each page
    for page in document:
        # Extract links
        link_list = page.get_links()
        for link in link_list:
            if link["kind"] == fitz.LINK_URI:
                # Check each regex pattern
                for regex in regex_patterns:
                    if regex.search(link["uri"]):
                        links.append(link["uri"])
                        break  # Stop checking other patterns once a match is found

    document.close()
    return links


def normalize_urls(doc, patterns):
    """
    Normalizes the links extracted from the document by removing duplicates and sorting them.
    """
    # Extract links from the document
    pdf_path = (
        doc["doc_file_metadata"]["file_directory"]
        + "/"
        + doc["doc_file_metadata"]["filename"]
    )
    extracted_links = extract_links_from_pdf(pdf_path=pdf_path, patterns=patterns)

    # Remove duplicates
    extracted_links = list(set(extracted_links))

    # Sort the links
    extracted_links.sort()

    # Update the document with the normalized links
    doc["doc_extracted_metadata"]["url"]["value"] = extracted_links
    doc["doc_extracted_metadata"]["url"]["source"] = "Post-processed from the document."

    return doc


def find_capabilities_and_services(
    input_text,
    capabilities_dict,
    source,
    capability_match_threshold=config.fuzzy_matching.capability_threshold,
    service_match_threshold=config.fuzzy_matching.service_threshold,
):
    capabilities_frequency = {}
    services_frequency = {}
    matched_phrases = []

    # Normalize and prepare the input text for sentence splitting
    input_text_normalized = re.sub(
        r"[^\w\s]", "", input_text.lower()
    )  # Remove non-word, non-space characters
    sentences = re.split(
        r"\.|\?|\!", input_text_normalized
    )  # Split text into sentences

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        words = sentence.split()

        # Process each capability based solely on the capability name
        for capability, services in capabilities_dict.items():
            capability_length = len(capability.split())
            capability_pattern = (
                r"\b" + re.escape(capability.lower()) + r"\b"
            )  # Match whole words only

            # Check for exact and fuzzy matches for capability
            for i in range(len(words) - capability_length + 1):
                current_phrase = " ".join(words[i : i + capability_length]).strip()
                if re.search(capability_pattern, current_phrase, re.IGNORECASE):
                    match_score = 100  # Exact match found
                else:
                    # Fuzzy matching when exact match is not found
                    match_score = fuzz.token_sort_ratio(
                        capability.lower().strip(), current_phrase.lower().strip()
                    )

                if match_score >= capability_match_threshold:
                    capabilities_frequency[capability] = (
                        capabilities_frequency.get(capability, 0) + 1
                    )
                    matched_phrases.append(
                        {
                            "type": "capability",
                            "capability": capability,
                            "name": capability,  # Name is the capability itself
                            "keyword": capability,  # Use capability name as keyword
                            "phrase": current_phrase,
                            "source": source,
                            "score": match_score,
                        }
                    )
                    print(
                        f"Matched Capability: {current_phrase} with {capability} (score: {match_score})"
                    )

            # Process each service and its keywords
            for service, keywords in services.items():
                for keyword in keywords:
                    keyword_length = len(keyword.split())
                    keyword_pattern = (
                        r"\b" + re.escape(keyword.lower()) + r"\b"
                    )  # Match whole words only

                    # Check for exact and fuzzy matches for services
                    for i in range(len(words) - keyword_length + 1):
                        current_phrase = " ".join(words[i : i + keyword_length]).strip()
                        if re.search(keyword_pattern, current_phrase, re.IGNORECASE):
                            match_score = 100  # Exact match found
                        else:
                            # Fuzzy matching when exact match is not found
                            match_score = fuzz.token_sort_ratio(
                                keyword.lower().strip(), current_phrase.lower().strip()
                            )

                        if match_score >= service_match_threshold:
                            services_frequency[service] = (
                                services_frequency.get(service, 0) + 1
                            )
                            matched_phrases.append(
                                {
                                    "type": "service",
                                    "capability": capability,
                                    "name": service,
                                    "keyword": keyword,
                                    "phrase": current_phrase,
                                    "source": source,
                                    "score": match_score,
                                }
                            )
                            print(
                                f"Matched Service: {current_phrase} with {keyword} (score: {match_score})"
                            )

    return capabilities_frequency, services_frequency, matched_phrases


def combine_and_sort(frequencies1, frequencies2):
    # Combine the frequencies and sum them if they exist in both dictionaries
    combined_frequencies = frequencies1.copy()
    for key, value in frequencies2.items():
        if key in combined_frequencies:
            combined_frequencies[key] += value
        else:
            combined_frequencies[key] = value

    # Sort the combined dictionary by frequency in descending order
    sorted_frequencies = {
        k: v
        for k, v in sorted(
            combined_frequencies.items(), key=lambda item: item[1], reverse=True
        )
    }
    return sorted_frequencies


def extract_metadata_values(metadata):
    def flatten_value(value):
        if isinstance(value, dict):
            return " ".join(flatten_value(v) for v in value.values())
        elif isinstance(value, list):
            return " ".join(flatten_value(item) for item in value)
        elif isinstance(value, str):
            if not value.endswith((".", "!", "?")):
                value += "."
            return value
        else:
            return str(value)

    concatenated_sentences = [
        flatten_value(value["value"])
        for key, value in metadata.items()
        if value["value"] != "not specified"
    ]
    return " ".join(concatenated_sentences)


def normalize_confidentiality(doc):
    # Load the document as a JSON object if it's passed as a string
    if isinstance(doc, str):
        doc = json.loads(doc)

    total_pages = len(doc["pages"])
    internal_use_count = 0
    confidential = ""
    # Check each page for the specified keywords
    for page in doc["pages"]:
        text = page["text_unstructured"].strip().lower()  # Clean and prepare text

        # Check for "Confidential"
        if "confidential" in text:
            confidential = "confidential"
            message = "Confidential keyword found."
            break

        # Check for "Internal Use Only"
        if "internal use only" in text:
            internal_use_count += 1

    # Determine if it meets the threshold for "Internal Use Only"
    if internal_use_count >= total_pages / 3:
        confidential = "internal use only"
        message = "No confidential keywords found, but Internal Use Only keyword found on more than 1/3 of the pages."
    else:
        confidential = "publicly available"
        message = "No confidential keywords found, and Internal Use Only keyword found on less than 1/3 of the pages."

    doc["doc_extracted_metadata"]["confidentiality"]["value"] = confidential
    doc["doc_extracted_metadata"]["confidentiality"]["source"] = (
        "Fixed in post-processing: " + message
    )

    print(f"{confidential=}, {message=}")

    return doc


def postprocess(doc):

    # Normalize null and empty strings
    doc = normalize_not_specified(doc)

    # Normalize document type
    doc = normalize_doc_type(doc)

    # Normalize year
    doc = normalize_year(doc)

    # Normalize URLs
    doc = normalize_urls(doc, config.postprocessing_behavior.url_patterns)
    # print(doc["doc_extracted_metadata"]["url"]["value"])

    # Normalize confidentiality
    doc = normalize_confidentiality(doc)

    # Normalize title
    title = doc["doc_extracted_metadata"]["title"]["value"]

    if title in ("", None, "not specified"):
        title = doc["doc_extracted_metadata"]["project_name"]["value"]

        if title in ("", None, "not specified"):
            title = doc["doc_file_metadata"]["filename"][:-4]

        doc["doc_extracted_metadata"]["title"]["value"] = title

    # Normalize industry names
    doc["doc_extracted_metadata"]["industry"]["value"] = normalize_industry(
        doc["doc_extracted_metadata"]["industry"]["value"]
    )

    # Normalize country
    doc["doc_extracted_metadata"]["country"]["value"] = normalize_country(
        doc["doc_extracted_metadata"]["country"]["value"]
    )

    # Normalize region
    doc["doc_extracted_metadata"]["region"]["value"] = normalize_region(
        doc["doc_extracted_metadata"]["region"]["value"]
    )

    # Normalize agency
    doc["doc_extracted_metadata"]["agency_name"]["value"] = normalize_agency(
        doc["doc_extracted_metadata"]["agency_name"]["value"]
    )

    # Normalize capabilities/services
    document_text = doc["doc_text_unstructured"].split(
        "\n\n\n####\nFile content: \n\n"
    )[1]
    metadata_text = extract_metadata_values(doc["doc_extracted_metadata"])

    doc_capabilities, doc_services, doc_phrases = find_capabilities_and_services(
        document_text, capabilities_services_dict, "document"
    )
    meta_capabilities, meta_services, meta_phrases = find_capabilities_and_services(
        metadata_text, capabilities_services_dict, "metadata"
    )

    combined_capabilities_freqs = combine_and_sort(doc_capabilities, meta_capabilities)
    combined_services_freqs = combine_and_sort(doc_services, meta_services)

    capabilities = (list(combined_capabilities_freqs.keys()),)
    services = (list(combined_services_freqs.keys()),)

    doc["doc_extracted_metadata"]["capabilities"]["value"] = capabilities
    doc["doc_extracted_metadata"]["services"]["value"] = services

    return doc
