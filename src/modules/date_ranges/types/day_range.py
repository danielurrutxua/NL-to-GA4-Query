import random
from ..constants.meses_espanol import meses_espanol

def generate_days_range(start_year, end_year, start_month, end_month, start_day, end_day):
    start_date = f"{start_year}-{start_month:02d}-{start_day:02d}"
    end_date = f"{end_year}-{end_month:02d}-{end_day:02d}"
    return start_date, end_date

def generate():
    start_year = random.randint(2010, 2022)
    end_year = random.randint(start_year, 2022)
    start_month = random.randint(1, 12)

    if start_year == end_year:
        end_month = random.randint(start_month, 12)
    else:
        end_month = random.randint(1, 12)

    start_day = random.randint(1, 20)
    if start_month == end_month and start_year == end_year:
        end_day = random.randint(start_day + 1, 28)
    else:
        end_day = random.randint(1, 28)

    variants = [
    "desde el {start_day} de {start_month_name} de {start_year} hasta el {end_day} de {end_month_name} de {end_year}",
    "del {start_day} de {start_month_name} de {start_year} al {end_day} de {end_month_name} de {end_year}",
    "entre el {start_day} de {start_month_name} de {start_year} y el {end_day} de {end_month_name} de {end_year}",
    "desde {start_day} de {start_month_name} de {start_year} hasta {end_day} de {end_month_name} de {end_year}",
    "del periodo del {start_day} de {start_month_name} de {start_year} al {end_day} de {end_month_name} de {end_year}"
    ]

    variants_same_month_year = [
        "del {start_day} al {end_day} de {start_month_name} de {start_year}"
    ]

    variants_same_year = [
        "del {start_day} de {start_month_name} al {end_day} de {end_month_name} de {start_year}"
    ]

    start_date, end_date = generate_days_range(start_year, end_year, start_month, end_month, start_day, end_day)
    chosen_variant = ""
    if start_year == end_year and start_month == end_month: chosen_variant = random.choice(variants_same_month_year)
    elif start_year == end_year: chosen_variant = random.choice(variants_same_year)
    else: chosen_variant = random.choice(variants)
    phrase = chosen_variant.format(
    start_day=start_day,
    start_month_name=meses_espanol[start_month-1],
    start_year=start_year,
    end_day=end_day,
    end_month_name=meses_espanol[end_month-1],
    end_year=end_year
)

    return phrase, {"startDate": start_date, "endDate": end_date}