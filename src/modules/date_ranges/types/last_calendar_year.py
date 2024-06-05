import random

def generate():
    variants = [
        "del último año",
        "del año pasado",
        "durante el último año",
        "en el último año",
        "a lo largo del último año",
        "correspondientes al último año",
        "registrados en el último año",
        "de los últimos doce meses",
        "del periodo del último año"
    ]
    phrase = random.choice(variants)
    return phrase, {"startDate": "lastCalendarYear", "endDate": "lastCalendarYear"}