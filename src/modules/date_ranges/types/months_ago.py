import random

def generate():
    num_months_ago = random.randint(2, 48)
    variants = [
        "de los últimos {num_months_ago} meses",
        "de hace {num_months_ago} meses",
        "durante los últimos {num_months_ago} meses",
        "en los últimos {num_months_ago} meses",
        "a lo largo de los últimos {num_months_ago} meses",
        "correspondientes a los últimos {num_months_ago} meses",
        "registrados en los últimos {num_months_ago} meses",
        "del periodo de los últimos {num_months_ago} meses"
    ]
    chosen_variant = random.choice(variants)
    phrase = chosen_variant.format(num_months_ago=num_months_ago)
    xMonthsAgo = str(num_months_ago*30) + 'daysAgo'
    return phrase, {"startDate": xMonthsAgo, "endDate": "today"}