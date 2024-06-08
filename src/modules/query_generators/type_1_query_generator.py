import random
from modules.query_generators.constants.initial_phrases import initial_phrases
from modules.query_generators.utils.resources import get_random_metric
from modules.date_ranges import generate as generate_date_ranges

def generate():
    # Seleccionar aleatoriamente una manera de comenzar la frase
    initial_phrase = random.choice(initial_phrases)

    # Seleccionar una métrica aleatoria
    metric = get_random_metric()
    metric_phrase = f"{metric.iloc[3]} {metric.iloc[1]}"

    # Seleccionar un tipo de rango de fecha aleatorio
    date_phrase, date_range_api_query = generate_date_ranges()

    natural_language_query = f"{initial_phrase} {metric_phrase.lower()} {date_phrase}."
    return (natural_language_query, {"metrics": [metric.iloc[0]], "dateRanges": [date_range_api_query]})
