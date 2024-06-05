import random

def generate():
    variants = [
        "del último mes",
        "del mes pasado",
        "durante el último mes",
        "en el último mes",
        "a lo largo del último mes",
        "correspondientes al último mes",
        "registrados en el último mes",
        "de los últimos treinta días",
        "del periodo del último mes"
    ]
    phrase = random.choice(variants)
    return phrase, {"startDate": "lastCalendarMonth", "endDate": "lastCalendarMonth"}