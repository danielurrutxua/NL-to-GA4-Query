import random

def generate():
    variants = [
        "de ayer",
        "del día de ayer",
        "en el día de ayer",
        "correspondientes a ayer",
        "registrados ayer",
        "durante el día de ayer",
        "a lo largo del día de ayer"
    ]
    phrase = random.choice(variants)
    return phrase, {"startDate": "yesterday", "endDate": "yesterday"}