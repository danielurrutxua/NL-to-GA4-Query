import random

def generate():
    num_years_ago = random.randint(2, 10)

    variants = [
        "de los últimos {num_years_ago} años",
        "de hace {num_years_ago} años",
        "durante los últimos {num_years_ago} años",
        "en los últimos {num_years_ago} años",
        "a lo largo de los últimos {num_years_ago} años",
        "correspondientes a los últimos {num_years_ago} años",
        "registrados en los últimos {num_years_ago} años",
        "del periodo de los últimos {num_years_ago} años"
    ]
    chosen_variant = random.choice(variants)
    phrase = chosen_variant.format(num_years_ago=num_years_ago)
    xYearsAgo = str(num_years_ago*365) + 'daysAgo'
    return phrase, {"startDate": xYearsAgo, "endDate": "today"}