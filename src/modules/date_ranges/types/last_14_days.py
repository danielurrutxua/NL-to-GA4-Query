import random

def generate():
    variants = [
        "de los últimos 14 días",
        "de las últimas dos semanas",
        "en los últimos 14 días",
        "durante los últimos 14 días",
        "a lo largo de los últimos 14 días",
        "correspondientes a los últimos 14 días",
        "registrados en los últimos 14 días",
        "del periodo de los últimos 14 días"
    ]
    phrase = random.choice(variants)
    return phrase, {"startDate": "last14days", "endDate": "last14days"}