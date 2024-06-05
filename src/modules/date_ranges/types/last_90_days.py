import random

def generate():
    variants = [
        "de los últimos 90 días",
        "de los últimos tres meses",
        "en los últimos 90 días",
        "durante los últimos 90 días",
        "a lo largo de los últimos 90 días",
        "correspondientes a los últimos 90 días",
        "registrados en los últimos 90 días",
        "del periodo de los últimos 90 días"
    ]
    phrase = random.choice(variants)
    return phrase, {"startDate": "last90days", "endDate": "last90days"}