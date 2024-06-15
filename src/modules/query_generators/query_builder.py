import random
from modules.query_generators.utils.resources import get_random_initial_phrase
from modules.query_generators.utils.resources import get_random_metric
from modules.query_generators.utils.resources import get_2_random_metrics
from modules.query_generators.utils.resources import get_random_dimension
from modules.dimension_filters import generate as get_random_dimension_filter
from modules.date_ranges import generate as get_random_date_range


def build_query():
    # Seleccionar aleatoriamente una manera de comenzar la frase
    phrase = get_random_initial_phrase()
    api_query = {}

    if random.getrandbits(1):
        phrase, api_query = set_metric(phrase, api_query)
    else:
        phrase, api_query = set_2_metrics(phrase, api_query)

    if random.getrandbits(1):
        phrase, api_query = set_dimension(phrase, api_query)

    if random.getrandbits(1):
        phrase, api_query = set_dimension_filter(phrase, api_query)

    phrase, api_query = set_date_range(phrase, api_query)

    return {"natural_language_query": phrase, "api_query": api_query}


def set_metric(phrase: str, api_query: dict):
    # Seleccionar una métrica aleatoria
    metric = get_random_metric()
    phrase += f" {metric.iloc[3]} {metric.iloc[1]}"
    api_query["metrics"] = [metric.iloc[0]]
    return phrase, api_query


def set_2_metrics(phrase: str, api_query: dict):
    # Seleccionar dos métricas aleatorias
    metrics = get_2_random_metrics()
    metric1, metric2 = metrics.iloc[0], metrics.iloc[1]
    metric_phrase1 = f"{metric1.iloc[3]} {metric1.iloc[1]}"
    metric_phrase2 = f"{metric2.iloc[3]} {metric2.iloc[1]}"
    phrase += f" {metric_phrase1.lower()} y {metric_phrase2.lower()}"
    api_query["metrics"] = [metric1.iloc[0], metric2.iloc[0]]
    return phrase, api_query


def set_dimension(phrase: str, api_query: dict):
    dimension = get_random_dimension()
    api_query["dimensions"] = [dimension.iloc[0]]
    phrase += f" por {dimension.iloc[1].lower()}"
    return phrase, api_query


def set_dimension_filter(phrase: str, api_query: dict):
    dimension_filter = get_random_dimension_filter()
    api_query["dimensionFilter"] = dimension_filter.iloc[0]
    phrase += f" {dimension_filter.iloc[1]}"
    return phrase, api_query


def set_date_range(phrase: str, api_query: dict):
    # Seleccionar un tipo de rango de fecha aleatorio
    date_phrase, date_range_api_query = get_random_date_range()
    api_query["dateRanges"] = [date_range_api_query]
    phrase += f" {date_phrase}"
    return phrase, api_query


# Ejemplo de uso
if __name__ == "__main__":
    result = build_query()
    print(result["natural_language_query"])
    print(result["api_query"])
