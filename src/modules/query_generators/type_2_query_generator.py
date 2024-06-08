import random
from modules.query_generators.constants.initial_phrases import initial_phrases
from modules.query_generators.utils.resources import get_2_random_metrics
from modules.date_ranges import generate as generate_date_ranges

def generate():
    # Seleccionar aleatoriamente una manera de comenzar la frase
    initial_phrase = random.choice(initial_phrases)

    # Seleccionar dos métricas aleatorias
    metrics = get_2_random_metrics()
    metric1, metric2 = metrics.iloc[0], metrics.iloc[1]
    metric_phrase1 = f"{metric1.iloc[3]} {metric1.iloc[1]}"
    metric_phrase2 = f"{metric2.iloc[3]} {metric2.iloc[1]}"

    # Seleccionar un tipo de rango de fecha aleatorio
    date_phrase, date_range_api_query = generate_date_ranges()

    # Construir la consulta en lenguaje natural
    natural_language_query = f"{initial_phrase} {metric_phrase1.lower()} y {metric_phrase2.lower()} {date_phrase}."
    
    # Devolver la consulta en lenguaje natural y la estructura de la API
    return (natural_language_query, {"metrics": [metric1.iloc[0], metric2.iloc[0]], "dateRanges": [date_range_api_query]})
