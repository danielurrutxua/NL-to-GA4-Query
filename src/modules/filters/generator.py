import random
from modules.utils.resources import get_random_english_word
from .constants.data_type_enum import DataType
from .constants.string_data_type.match_type_string_enum import MatchTypeString
from .constants.equal_variants import variants as equal_variants
from .constants.string_data_type.begins_with_variants import variants_begins_with
from .constants.string_data_type.ends_with_variants import variants_ends_with
from .constants.string_data_type.contains_variants import variants_contains
from .constants.integer_data_type.match_type_integer_enum import MatchTypeInteger
from .constants.integer_data_type.greater_than_variants import variants_greater_than
from .constants.integer_data_type.less_than_variants import variants_less_than
from .constants.integer_data_type.greater_than_or_equal_variants import (
    variants_greater_than_or_equal_to,
)
from .constants.integer_data_type.less_than_or_equal_variants import (
    variants_less_than_or_equal_to,
)


def generate(dimension_or_metric):
    match random.choice(list(DataType)):
        case DataType.STRING:
            return generate_string_type_filter(dimension_or_metric)
        case DataType.NUMERIC:
            return generate_numeric_type_filter(dimension_or_metric)


def generate_string_type_filter(dimension_or_metric):
    phrase = ""
    match_type = ""
    value = get_random_english_word().iloc[0]
    match random.choice(list(MatchTypeString)):
        case MatchTypeString.EXACT:
            variant = random.choice(equal_variants)
            phrase = variant.format(object=random.choice([syn.strip() for syn in dimension_or_metric.iloc[3].split(',')]), value=value)
            match_type = MatchTypeString.EXACT.name
        case MatchTypeString.BEGINS_WITH:
            variant = random.choice(variants_begins_with)
            phrase = variant.format(object=random.choice([syn.strip() for syn in dimension_or_metric.iloc[3].split(',')]), value=value)
            match_type = MatchTypeString.BEGINS_WITH.name
        case MatchTypeString.ENDS_WITH:
            variant = random.choice(variants_ends_with)
            phrase = variant.format(object=random.choice([syn.strip() for syn in dimension_or_metric.iloc[3].split(',')]), value=value)
            match_type = MatchTypeString.ENDS_WITH.name
        case MatchTypeString.CONTAINS:
            variant = random.choice(variants_contains)
            phrase = variant.format(object=random.choice([syn.strip() for syn in dimension_or_metric.iloc[3].split(',')]), value=value)
            match_type = MatchTypeString.CONTAINS.name

    api_query = {
        "filter": {
            "fieldName": dimension_or_metric.iloc[0],
            "stringFilter": {"matchType": match_type, "value": value},
        }
    }

    return phrase, api_query


def generate_numeric_type_filter(dimension_or_metric):
    phrase = ""
    match_type = ""
    value = random.randint(0, 1000)
    match random.choice(list(MatchTypeInteger)):
        case MatchTypeInteger.EQUALS:
            variant = random.choice(equal_variants)
            phrase = variant.format(object=dimension_or_metric.iloc[1], value=value)
            match_type = MatchTypeInteger.EQUALS.name
        case MatchTypeInteger.GREATER_THAN:
            variant = random.choice(variants_greater_than)
            phrase = variant.format(object=dimension_or_metric.iloc[1], value=value)
            match_type = MatchTypeInteger.GREATER_THAN.name
        case MatchTypeInteger.LESS_THAN:
            variant = random.choice(variants_less_than)
            phrase = variant.format(object=dimension_or_metric.iloc[1], value=value)
            match_type = MatchTypeInteger.LESS_THAN.name
        case MatchTypeInteger.GREATER_THAN_OR_EQUAL:
            variant = random.choice(variants_greater_than_or_equal_to)
            phrase = variant.format(object=dimension_or_metric.iloc[1], value=value)
            match_type = MatchTypeInteger.GREATER_THAN_OR_EQUAL.name
        case MatchTypeInteger.LESS_THAN_OR_EQUAL:
            variant = random.choice(variants_less_than_or_equal_to)
            phrase = variant.format(object=dimension_or_metric.iloc[1], value=value)
            match_type = MatchTypeInteger.LESS_THAN_OR_EQUAL.name

    api_query = {
        "filter": {
            "fieldName": dimension_or_metric.iloc[0],
            "numericFilter": {"operation": match_type, "value": {"int64Value": value}},
        }
    }

    return phrase, api_query
