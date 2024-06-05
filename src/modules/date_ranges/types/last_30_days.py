import random

def generate():
    variants = [
        "de los últimos 30 días",
        "del último mes",
        "en los últimos 30 días",
        "durante los últimos 30 días",
        "a lo largo de los últimos 30 días",
        "correspondientes a los últimos 30 días",
        "registrados en los últimos 30 días",
        "del periodo de los últimos 30 días"
    ]
    phrase = random.choice(variants)
    return phrase, {"startDate": "last30days", "endDate": "last30days"}