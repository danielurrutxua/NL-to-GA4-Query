import random

def generate():
    num_days_ago = random.randint(2, 200)

    variants = [
        "de los últimos {num_days_ago} días",
        "de hace {num_days_ago} días",
        "durante los últimos {num_days_ago} días",
        "en los últimos {num_days_ago} días",
        "a lo largo de los últimos {num_days_ago} días",
        "correspondientes a los últimos {num_days_ago} días",
        "registrados en los últimos {num_days_ago} días",
        "del periodo de los últimos {num_days_ago} días"
    ]
    xDaysAgo = str(num_days_ago) + 'DaysAgo'
    chosen_variant = random.choice(variants)
    phrase = chosen_variant.format(num_days_ago=num_days_ago)
    return phrase, {"startDate": xDaysAgo, "endDate": "today"}