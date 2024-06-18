import random

def generate():
    num_weeks_ago = random.randint(2, 200)
    variants = [
        "de las últimas {num_weeks_ago} semanas",
        "de hace {num_weeks_ago} semanas",
        "durante las últimas {num_weeks_ago} semanas",
        "en las últimas {num_weeks_ago} semanas",
        "a lo largo de las últimas {num_weeks_ago} semanas",
        "correspondientes a las últimas {num_weeks_ago} semanas",
        "registrados en las últimas {num_weeks_ago} semanas",
        "del periodo de las últimas {num_weeks_ago} semanas"
    ]
    xWeeksAgo = str(num_weeks_ago*7) + 'daysAgo'
    chosen_variant = random.choice(variants)
    phrase = chosen_variant.format(num_weeks_ago=num_weeks_ago)
    return phrase, {"startDate": xWeeksAgo, "endDate": "today"}