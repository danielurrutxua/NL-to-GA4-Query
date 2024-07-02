import random
from modules.utils.resources import get_random_initial_phrase
from modules.utils.resources import get_random_metric
from modules.utils.resources import get_2_random_metrics
from modules.utils.resources import get_random_dimension
from modules.filters import get_random_filter
from modules.date_ranges import get_random_date_range


def build_query(filtros, fechas):
    phrase = get_random_initial_phrase()
    api_query = {}

    if random.getrandbits(1):
        phrase, api_query = set_metric(phrase, api_query)
    else:
        phrase, api_query = set_2_metrics(phrase, api_query)

    if random.getrandbits(1):
        phrase, api_query = set_dimension(phrase, api_query)

    if filtros == 'y':
        phrase, api_query = set_filters(phrase, api_query)
    
    if fechas == 'y':
        phrase, api_query = set_date_range(phrase, api_query)

    return {"natural_language_query": phrase, "api_query": api_query}


def set_metric(phrase: str, api_query: dict):
    metric = get_random_metric()
    synonym = random.choice([syn.strip() for syn in metric.iloc[3].split(',')])
    phrase += f" {synonym}".lower()
    api_query["metrics"] = [metric.iloc[0]]
    return phrase, api_query


def set_2_metrics(phrase: str, api_query: dict):
    metrics = get_2_random_metrics()
    metric1, metric2 = metrics.iloc[0], metrics.iloc[1]
    synonym_metric1 = random.choice([syn.strip() for syn in metric1.iloc[3].split(',')])
    synonym_metric2 = random.choice([syn.strip() for syn in metric2.iloc[3].split(',')])
    metric_phrase1 = f"{synonym_metric1}"
    metric_phrase2 = f"{synonym_metric2}"
    phrase += f" {metric_phrase1.lower()} y {metric_phrase2.lower()}"
    api_query["metrics"] = [metric1.iloc[0], metric2.iloc[0]]
    return phrase, api_query


def set_dimension(phrase: str, api_query: dict):
    dimension = get_random_dimension()
    api_query["dimensions"] = [dimension.iloc[0]]
    synonym = random.choice([syn.strip() for syn in dimension.iloc[3].split(',')])
    phrase += f" por {synonym.lower()}"
    return phrase, api_query

def set_filters(phrase: str, api_query: dict):
    actions = [None, "dimension", "metric", "both"]
    
    action = random.choice(actions)
    
    if action is None:
        return phrase, api_query
    elif action == "dimension":
        phrase, api_query = set_dimension_filter(phrase, api_query)
    elif action == "metric":
        phrase, api_query = set_metric_filter(phrase, api_query)
    elif action == "both":
        if random.choice([True, False]):
            phrase, api_query = set_dimension_filter(phrase, api_query)
            phrase += " y"
            phrase, api_query = set_metric_filter(phrase, api_query)
        else:
            phrase, api_query = set_metric_filter(phrase, api_query)
            phrase += " y"
            phrase, api_query = set_dimension_filter(phrase, api_query)
    
    return phrase, api_query

def set_dimension_filter(phrase: str, api_query: dict):
    phrase_filter_content, api_query_filter_content = get_random_filter(get_random_dimension())
    api_query["dimensionFilter"] = api_query_filter_content
    phrase += f" {phrase_filter_content}".lower()
    return phrase, api_query

def set_metric_filter(phrase: str, api_query: dict):
    phrase_filter_content, api_query_filter_content = get_random_filter(get_random_metric())
    api_query["metricFilter"] = api_query_filter_content
    phrase += f" {phrase_filter_content}".lower()
    return phrase, api_query


def set_date_range(phrase: str, api_query: dict):
    date_phrase, date_range_api_query = get_random_date_range()
    api_query["dateRanges"] = [date_range_api_query]
    phrase += f" {date_phrase}"
    return phrase, api_query
