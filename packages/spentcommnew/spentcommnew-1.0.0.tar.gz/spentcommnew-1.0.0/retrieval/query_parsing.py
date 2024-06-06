import re
from datetime import datetime
from dateutil.relativedelta import relativedelta
import spacy
import re
import inflect
from fuzzywuzzy import fuzz
from spacy.matcher import PhraseMatcher

import sys

root_dir = "/home/jupyter/code/sapient/knowledge-powerhouse-pocss"
sys.path.append(str(root_dir))


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


# Load English language model
nlp = spacy.load("en_core_web_sm")  # This model includes a lemmatizer


def parse_years_from_query(query):
    current_year = datetime.now().year
    years_result = {}

    # Mapping between words and numbers up to twelve
    word_to_number = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
    }

    # Function to convert words to numbers
    def words_to_numbers(text):
        words = text.lower().split()
        numbers = [word_to_number[word] for word in words if word in word_to_number]
        return sum(numbers) if numbers else None

    # Handle 'the last X years' using word-to-number mapping
    match_last_years = re.search(
        r"(?:last|past)\s+(\w+)\s+years?", query, re.IGNORECASE
    )
    if match_last_years:
        last_years_text = match_last_years.group(1)
        last_years = words_to_numbers(last_years_text)
        if last_years:
            years_ago = last_years
            years_result["gte"] = current_year - years_ago + 1  # Adjust start year

    # Rest of the code remains unchanged
    specific_years = re.findall(r"\b\d{4}\b", query)
    specific_years = [
        year for year in specific_years if year.startswith(("20", "19"))
    ]  # Filter years starting with 20 or 19
    if specific_years:
        if "or" in query or "and" in query:
            years_result["eq"] = list(map(int, specific_years))
        elif "-" not in query and "to" not in query:
            years_result["eq"] = [int(specific_years[0])]

    ranges_years = re.findall(
        r"(\d+)\s*(?:-|to|through|/|&)\s*(\d+)", query, re.IGNORECASE
    )
    if ranges_years:
        start, end = map(int, ranges_years[0])
        if start > end:
            start, end = end, start
        if end < 100 or start < 100:  # Check if either start or end year is two-digit
            start, end = adjust_two_digit_years(start, end, current_year)
        years_result["gte"] = start
        years_result["lte"] = end
        if years_result["lte"] < years_result["gte"]:
            years_result["lte"], years_result["gte"] = (
                years_result["gte"],
                years_result["lte"],
            )  # Swap if lte < gte

    ranges_months = re.findall(
        r"(\d+)\s*months?", query, re.IGNORECASE
    )  # Modified regex to include optional "s" after "month"
    if ranges_months:
        months_ago = int(ranges_months[0])
        end_date = datetime.now() - relativedelta(months=months_ago)
        years_result["gte"] = end_date.year

    if "last year" in query or "past year" in query:
        years_result["gte"] = current_year - 1

    if "this year" in query:
        years_result["eq"] = [current_year]

    if "next year" in query:
        years_result["eq"] = [current_year + 1]

    match_last_years = re.search(
        r"(?:last|past)\s+(\d+)\s+years?", query, re.IGNORECASE
    )
    if match_last_years:
        years_ago = int(match_last_years.group(1))
        years_result["gte"] = current_year - years_ago

    match_since = re.search(r"since\s+(\d{4})", query)
    if match_since:
        years_result["gte"] = int(match_since.group(1))
        years_result.pop("eq", None)

    match_until = re.search(r"until\s+(\d{4})", query)
    if match_until:
        years_result["lte"] = int(match_until.group(1))
        years_result.pop("eq", None)

    match_within = re.search(r"within\s+the\s+next\s+(\d+)\s+years", query)
    if match_within:
        years_within = int(match_within.group(1))
        years_result["gte"] = current_year
        years_result["lte"] = current_year + years_within

    match_no_later_than = re.search(r"no\s+later\s+than\s+(\d{4})", query)
    if match_no_later_than:
        years_result["lte"] = int(match_no_later_than.group(1))
        years_result.pop("eq", None)

    match_before = re.search(r"before\s+(\d{4})", query)
    if match_before:
        years_result["lt"] = int(match_before.group(1))
        years_result.pop("eq", None)

    if "lte" in years_result:
        if len(str(years_result["lte"])) == 2:
            years_result["lte"] = int("20" + str(years_result["lte"]))

    match_between = re.search(
        r"between\s+(\d{4})\s*(?:-|to|and|through|/|&)\s*(\d{2,4})",
        query,
        re.IGNORECASE,
    )
    if match_between:
        start, end = map(int, match_between.groups())
        if start > end:
            start, end = end, start
        if end < 100 or start < 100:  # Check if either start or end year is two-digit
            start, end = adjust_two_digit_years(start, end, current_year)
        years_result["gte"] = start
        years_result["lte"] = end
        if years_result["lte"] < years_result["gte"]:
            years_result["lte"], years_result["gte"] = (
                years_result["gte"],
                years_result["lte"],
            )  # Swap if lte < gte
        years_result.pop("eq", None)

    match_between_or_later = re.search(
        r"from\s+(\d{4})\s+or\s+later", query, re.IGNORECASE
    )
    if match_between_or_later:
        years_result["gte"] = int(match_between_or_later.group(1))
        years_result.pop("eq", None)

    match_after = re.search(r"after\s+(\d{4})", query, re.IGNORECASE)
    if match_after:
        years_result["gt"] = int(match_after.group(1))
        years_result.pop("eq", None)

    match_before_but_after = re.search(
        r"before\s+(\d{4})\s+but\s+after\s+(\d{4})", query, re.IGNORECASE
    )
    if match_before_but_after:
        before_year = int(match_before_but_after.group(1))
        after_year = int(match_before_but_after.group(2))
        years_result["lt"] = before_year
        years_result["gt"] = after_year

    match_prior_to = re.search(r"prior\s+to\s+(\d{4})", query, re.IGNORECASE)
    if match_prior_to:
        years_result["lt"] = int(match_prior_to.group(1))
        years_result.pop("eq", None)

    match_prior = re.search(r"prior\s+(\d{4})", query, re.IGNORECASE)
    if match_prior:
        prior_year = int(match_prior.group(1))
        years_result["lt"] = prior_year
        if "eq" in years_result:
            years_result.pop("eq")

    match_post = re.search(r"post\s+(\d{4})", query, re.IGNORECASE)
    if match_post:
        post_year = int(match_post.group(1))
        years_result["gt"] = post_year
        if "eq" in years_result:
            years_result.pop("eq")

    match_after = re.search(r"after\s+(\d{4})", query, re.IGNORECASE)
    if match_after:
        after_year = int(match_after.group(1))
        years_result["gt"] = after_year
        if "eq" in years_result:
            years_result.pop("eq")

    return years_result


def adjust_two_digit_years(start, end, current_year):
    if end < 100:  # Check if end year is two-digit
        end += current_year // 100 * 100  # Adjust end year to current century
        if end >= current_year:  # Adjust for years in the past
            end -= 100
    if start < 100:  # Check if start year is two-digit
        start += current_year // 100 * 100  # Adjust start year to current century
        if start > current_year:  # Adjust for years in the future
            start -= 100
    return start, end


def create_phrase_matcher(nlp, terms_dict):
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    p = inflect.engine()

    for key, patterns in terms_dict.items():
        # Register each key in the vocab
        nlp.vocab.strings.add(key)

        # Generate both singular and plural forms
        extended_patterns = []
        for text in patterns:
            doc = nlp.make_doc(text)
            extended_patterns.append(doc)

            # Generate plural form and make a doc if different
            plural_text = p.plural(text)
            if plural_text.lower() != text.lower():
                plural_doc = nlp.make_doc(plural_text)
                extended_patterns.append(plural_doc)

            # Generate singular form and make a doc if different
            singular_text = p.singular_noun(text)
            if singular_text and singular_text.lower() != text.lower():
                singular_doc = nlp.make_doc(singular_text)
                extended_patterns.append(singular_doc)

        matcher.add(key, extended_patterns)
    return matcher


# Assuming dictionaries for agencies, regions, industries, and countries are predefined
# Instantiate matchers
agency_matcher = create_phrase_matcher(nlp, agencies_dict)
region_matcher = create_phrase_matcher(nlp, regions_dict)
industry_matcher = create_phrase_matcher(nlp, industries_dict)
country_matcher = create_phrase_matcher(nlp, countries_dict)


def parse_query_capabilities_services(query, threshold=config.fuzzy_matching.threshold):
    matched_capabilities = set()
    matched_services = set()
    matched_texts = {}  # Store matched texts for further analysis

    # Normalize the query for case-insensitive matching
    modified_query = query.lower()

    # Function to remove matched term using regex for precise matching
    def remove_matched_term(query, term):
        pattern = re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
        return re.sub(pattern, "", query)

    # Match capabilities explicitly found in the query
    for capability, services_dict in capabilities_services_dict.items():
        if fuzz.partial_ratio(capability.lower(), modified_query) > threshold:
            # print(
            #     f"Matched capability: {capability} with query: {modified_query} with score: {fuzz.partial_ratio(capability.lower(), modified_query)}"
            # )
            matched_capabilities.add(capability)
            # Remove the matched capability to prevent it influencing further matches
            modified_query = remove_matched_term(modified_query, capability)

    # Match services and check if their parent capability has already been matched
    for capability, services_dict in capabilities_services_dict.items():
        for service, variations in services_dict.items():
            for variation in variations:
                if fuzz.partial_ratio(variation.lower(), modified_query) > threshold:
                    matched_services.add(service)
                    matched_capabilities.add(capability)  # Store matched capability
                    # Store matched texts for debugging or analysis
                    matched_texts[service] = (
                        variation  # Store matched variation for review
                    )
                    # Remove matched service to clean up the query for subsequent matches
                    modified_query = remove_matched_term(modified_query, variation)

    return {
        "capabilities": list(matched_capabilities),
        "services": list(matched_services),
        "matched_texts": matched_texts,
        "modified_query": modified_query.strip(),
    }


def parse_query_ner(query):

    entities = {
        "agency_name": [],
        "region": [],
        "industry": [],
        "country": [],
        "capabilities": [],
        "services": [],
        "year": [],
    }

    doc = nlp(query)  # Convert query to a Spacy document once to use it multiple times

    # Match and normalize entities using PhraseMatchers for regions
    region_matches = region_matcher(doc)
    regions_text = []
    for match_id, start, end in region_matches:
        key = nlp.vocab.strings[match_id]
        matched_text = doc[start:end].text  # Capture the exact text that matched
        if key not in entities["region"]:  # Add key to avoid duplicates
            entities["region"].append(key)
            regions_text.append(matched_text)

    # Remove identified regions from the query string
    for region in regions_text:
        query = re.sub(re.escape(region), "", query, flags=re.IGNORECASE)

    # Similar extraction and removal can be performed for other entities
    # For example, countries
    doc = nlp(query)
    country_matches = country_matcher(doc)
    countries_text = []
    for match_id, start, end in country_matches:
        key = nlp.vocab.strings[match_id]
        matched_text = doc[start:end].text  # Capture the exact text that matched
        if key not in entities["country"]:  # Add key to avoid duplicates
            entities["country"].append(key)
            countries_text.append(matched_text)

    # Remove identified countries from the query string
    for country in countries_text:
        query = re.sub(re.escape(country), "", query, flags=re.IGNORECASE)

    # Match and normalize capabilities and services
    capabilities_services_result = parse_query_capabilities_services(query)

    entities["capabilities"] = capabilities_services_result["capabilities"]
    entities["services"] = capabilities_services_result["services"]

    # Remove identified capabilities and services from the query string
    query = capabilities_services_result["modified_query"]

    # Match and normalize entities using PhraseMatchers for industries
    for matcher, category in zip(
        [agency_matcher, industry_matcher], ["agency_name", "industry"]
    ):
        matches = matcher(nlp(query))
        for match_id, start, end in matches:
            key = nlp.vocab.strings[match_id]
            if key not in entities[category]:  # Add key to avoid duplicates
                entities[category].append(key)

    # Extract years from the query
    years_result = parse_years_from_query(query)
    entities["year"] = years_result

    return entities


import re


def replace_acronyms(text, acronym_dict):
    # Create a regular expression pattern to match acronyms with case insensitivity
    pattern = re.compile(r"\b(" + "|".join(acronym_dict.keys()) + r")\b", re.IGNORECASE)

    # Replace acronyms with full forms
    replaced_text = pattern.sub(lambda x: acronym_dict[x.group().upper()], text)

    return replaced_text


def replace_synonyms(text, synonyms_dict):
    # Replace synonyms with their corresponding keys with case insensitivity
    for key, synonyms_list in synonyms_dict.items():
        for synonym in synonyms_list:
            # Using regular expression to match whole words only with case insensitivity
            pattern = re.compile(r"\b" + re.escape(synonym) + r"\b", re.IGNORECASE)
            text = pattern.sub(key, text)

    return text


def preprocess_query(query):

    # Replace acronyms and synonyms
    query = replace_acronyms(query, acronym_to_full_names_dict)
    query = replace_synonyms(query, synonyms)

    tokens = []
    temp_token = ""
    in_quote = False
    quote_char = ""
    field_value_pairs = {}
    pending_field_name = ""

    recognized_fields = [
        "file_name",
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
        "partners_involved",
    ]

    i = 0
    while i < len(query):
        char = query[i]

        if (
            (char in ["'", '"']) and not in_quote and not pending_field_name
        ):  # Start of quoted token not for field
            in_quote = True
            quote_char = char
            temp_token += char
        elif (
            (char in ["'", '"']) and not in_quote and pending_field_name
        ):  # Start of quoted field value
            in_quote = True
            quote_char = char
            temp_token += char  # This will capture the quote for the field value
        elif char == quote_char and in_quote:  # End of quoted token
            temp_token += char
            if pending_field_name:
                # Accumulate values in a list for each field
                if pending_field_name in field_value_pairs:
                    field_value_pairs[pending_field_name].append(
                        temp_token.strip(quote_char)
                    )
                else:
                    field_value_pairs[pending_field_name] = [
                        temp_token.strip(quote_char)
                    ]
                pending_field_name = ""
            else:
                tokens.append(temp_token)
            temp_token = ""
            in_quote = False
            quote_char = ""
        elif (
            char == " " and not in_quote and not pending_field_name
        ):  # Space delimits tokens outside quotes and fields
            if temp_token:
                tokens.append(temp_token)
                temp_token = ""
        elif (
            char == ":" and temp_token in recognized_fields
        ):  # Detecting field-value pair
            pending_field_name = (
                temp_token  # Mark the field name for next value capture
            )
            temp_token = ""
        else:
            temp_token += char  # Accumulate characters into token

        i += 1

    # Catch any trailing token not followed by a space or end of quote
    if temp_token:
        if pending_field_name:
            if pending_field_name in field_value_pairs:
                field_value_pairs[pending_field_name].append(temp_token)
            else:
                field_value_pairs[pending_field_name] = [temp_token]
        else:
            tokens.append(temp_token)

    should_have_keywords, excluded_keywords, quoted_keywords = [], [], []
    cleaned_query = []

    for token in tokens:
        if token.startswith("-"):
            if token.startswith("-'") or token.startswith(
                '-"'
            ):  # Exclude quoted keyword
                excluded_keywords.append(token[2:-1])
            else:  # Exclude unquoted keyword
                excluded_keywords.append(token[1:])
        elif token.startswith("+"):
            if token.startswith("+'") or token.startswith(
                '+"'
            ):  # Include quoted must-have keyword
                should_have_keywords.append(token[2:-1])
                cleaned_query.append(token[2:-1])
            else:  # Include unquoted must-have keyword
                should_have_keywords.append(token[1:])
                cleaned_query.append(token[1:])
        elif token.startswith("'") or token.startswith(
            '"'
        ):  # Quoted keyword, not a field value
            quoted_keywords.append(token[1:-1])
            cleaned_query.append(token[1:-1])
        else:
            cleaned_query.append(token)

    cleaned_query_string = " ".join(cleaned_query)

    # If cleaned_query_string is empty, replace it with the values from field_value_pairs
    if not cleaned_query_string:
        # Join the values from field_value_pairs with a space. Adjust as needed for your use case.
        field_values = " ".join([" ".join(vals) for vals in field_value_pairs.values()])
        cleaned_query_string = field_values

    return (
        cleaned_query_string,
        quoted_keywords,
        should_have_keywords,
        excluded_keywords,
        field_value_pairs,
    )
