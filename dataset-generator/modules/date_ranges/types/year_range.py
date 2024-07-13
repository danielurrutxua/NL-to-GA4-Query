import random

def generate_years_range(start_year, end_year):
    start_date = f"{start_year}-01-01"
    end_date = f"{end_year}-12-31"
    return start_date, end_date

def generate():
    start_year = random.randint(2000, 2023)
    end_year = random.randint(start_year + 1, 2024)
    start_date, end_date = generate_years_range(start_year, end_year)
    range_variants = [
    "desde {start_year} hasta {end_year}",
    "de {start_year} a {end_year}",
    "del {start_year} al {end_year}",
    "entre {start_year} y {end_year}",
    "desde el año {start_year} hasta el año {end_year}",
    "desde el año {start_year} hasta {end_year}"
    "del año {start_year} al año {end_year}",
    "de {start_year} hasta {end_year}"
    ]
    variant = random.choice(range_variants)
    phrase = variant.format(start_year=start_year, end_year=end_year)

    return phrase, {"startDate": start_date, "endDate": end_date}