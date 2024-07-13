import random

def generate_year_range(year):
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    return start_date, end_date

def generate():
    year = random.randint(2000, 2024)
    start_date, end_date = generate_year_range(year)
    variants = [
        "en",
        "de",
        "durante",
        "para",
        "del año",
        "en el año",
        "correspondientes a",
        "registrados en",
        "durante el año",
        "para el año",
        "a lo largo de",
        "del periodo de"
    ]
    chosen_variant = random.choice(variants)
    phrase = f"{chosen_variant} {year}"

    return phrase, {"startDate": start_date, "endDate": end_date}