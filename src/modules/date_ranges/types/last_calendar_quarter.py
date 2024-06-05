import random

def generate():
    variants = [
        "del último trimestre",
        "del trimestre pasado",
        "durante el último trimestre",
        "en el último trimestre",
        "a lo largo del último trimestre",
        "correspondientes al último trimestre",
        "registrados en el último trimestre",
        "de los últimos tres meses",
        "del periodo del último trimestre"
    ]
    phrase = random.choice(variants)
    return phrase, {"startDate": "lastCalendarQuarter", "endDate": "lastCalendarQuarter"}