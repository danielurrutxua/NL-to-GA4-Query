import random

def generate():
    variants = [
        "de los últimos 7 días",
        "de la última semana",
        "en los últimos 7 días",
        "durante los últimos 7 días",
        "a lo largo de los últimos 7 días",
        "correspondientes a los últimos 7 días",
        "registrados en los últimos 7 días",
        "del periodo de los últimos 7 días"
    ]
    phrase = random.choice(variants)
    return phrase, {"startDate": "last7days", "endDate": "last7days"}