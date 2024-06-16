import random
from ..query_generators.utils.resources import get_random_dimension
from .constants.data_type_enum import DataType
from .constants.comparison_type_string_enum import ComparisonTypeString
from .constants.equal_variants import variants as equal_variants
from .constants.begins_with_variants import variants_begins_with
from .constants.ends_with_variants import variants_ends_with
from .constants.contains_variants import variants_contains


def generate():
    dimension = get_random_dimension()

    return generate_string_type_filter(dimension)


def generate_string_type_filter(dimension):
    phrase = ""
    match_type = ""
    value = "andom_va;ue"
    match random.choice(list(ComparisonTypeString)):
        case ComparisonTypeString.EXACT:
            variant = random.choice(equal_variants)
            phrase = variant.format(object=dimension.iloc[1], value=value)
            match_type = ComparisonTypeString.EXACT.name
        case ComparisonTypeString.BEGINS_WITH:
            variant = random.choice(variants_begins_with)
            phrase = variant.format(object=dimension.iloc[1], value=value)
            match_type = ComparisonTypeString.BEGINS_WITH.name
        case ComparisonTypeString.ENDS_WITH:
            variant = random.choice(variants_ends_with)
            phrase = variant.format(object=dimension.iloc[1], value=value)
            match_type = ComparisonTypeString.ENDS_WITH.name
        case ComparisonTypeString.CONTAINS:
            variant = random.choice(variants_contains)
            phrase = variant.format(object=dimension.iloc[1], value=value)
            match_type = ComparisonTypeString.CONTAINS.name

    api_query = {
        "filter": {
            "fieldName": dimension.iloc[0],
            "stringFilter": {"matchType": match_type, "value": value},
        }
    }

    return phrase, api_query
