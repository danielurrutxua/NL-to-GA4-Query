import random

def generate():
    variants = [
        "de la última semana",
        "de la semana pasada",
        "durante la última semana",
        "en la última semana",
        "a lo largo de la última semana",
        "correspondientes a la última semana",
        "registrados en la última semana",
        "de los últimos siete días",
        "del periodo de la última semana"
    ]
    phrase = random.choice(variants)
    return phrase, {"startDate": "lastCalendarWeek", "endDate": "lastCalendarWeek"}