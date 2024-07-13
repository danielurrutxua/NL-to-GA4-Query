import random
from ..constants.meses_espanol import meses_espanol

def generate_day_range(year, month, day):
    start_date = f"{year}-{month:02d}-{day:02d}"
    end_date = start_date  # Para un solo día, la fecha de inicio y fin son las mismas
    return start_date, end_date

def generate():
    year = random.randint(2010, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Para simplificar, asumimos un máximo de 28 días
    start_date, end_date = generate_day_range(year, month, day)

    variants = [
    "el día {day} de {month_name} de {year}",
    "en el {day} de {month_name} de {year}",
    "para el {day} de {month_name} de {year}",
    "del día {day} de {month_name} de {year}",
    "del {day} de {month_name} de {year}",
    "registrados el {day} de {month_name} de {year}",
    "correspondientes al {day} de {month_name} de {year}",
    "durante el {day} de {month_name} de {year}",
    "a lo largo del {day} de {month_name} de {year}"
]

    chosen_variant = random.choice(variants)
    phrase = chosen_variant.format(day=day, month_name=meses_espanol[month-1], year=year)

    return phrase, {"startDate": start_date, "endDate": end_date}