import random

def generate():
    variants = [
        "de hoy",
        "del día de hoy",
        "en el día de hoy",
        "correspondientes a hoy",
        "registrados hoy",
        "durante el día de hoy",
        "a lo largo del día de hoy"
    ]
    phrase = random.choice(variants)
    return phrase, {"startDate": "today", "endDate": "today"}