import random
from ..constants.meses_espanol import meses_espanol

def generate_month_range(month, year):
    start_date = f"{year}-{month:02d}-01"

    if month == 1:  # Enero
        end_date = f"{year}-01-31"
    elif month == 2:  # Febrero
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            end_date = f"{year}-02-29"  # Año bisiesto
        else:
            end_date = f"{year}-02-28"
    elif month == 3:  # Marzo
        end_date = f"{year}-03-31"
    elif month == 4:  # Abril
        end_date = f"{year}-04-30"
    elif month == 5:  # Mayo
        end_date = f"{year}-05-31"
    elif month == 6:  # Junio
        end_date = f"{year}-06-30"
    elif month == 7:  # Julio
        end_date = f"{year}-07-31"
    elif month == 8:  # Agosto
        end_date = f"{year}-08-31"
    elif month == 9:  # Septiembre
        end_date = f"{year}-09-30"
    elif month == 10:  # Octubre
        end_date = f"{year}-10-31"
    elif month == 11:  # Noviembre
        end_date = f"{year}-11-30"
    elif month == 12:  # Diciembre
        end_date = f"{year}-12-31"
    return start_date, end_date

def generate():
    year = random.randint(2000, 2024)
    month = random.randint(1, 12)
    start_date, end_date = generate_month_range(month, year)

    variants = [
        "en el mes de {month_name} de {year}",
        "durante el mes de {month_name} de {year}",
        "para el mes de {month_name} de {year}",
        "del mes de {month_name} de {year}",
        "en {month_name} de {year}",
        "en {month_name} {year}",
        "de {month_name} de {year}",
        "de {month_name} {year}",
        "correspondientes al mes de {month_name} de {year}",
        "registrados en el mes de {month_name} de {year}",
        "a lo largo del mes de {month_name} de {year}",
        "del periodo de {month_name} de {year}",
        "el mes de {month_name} del año {year}",
        "mes de {month_name} del año {year}",
        "en el mes del año {year} correspondiente a {month_name}",
        "en el mes de {month_name} del {year}",
        "durante el mes de {month_name} del {year}",
        "para el mes de {month_name} del {year}",
        "del mes de {month_name} del {year}",
        "en {month_name} del {year}",
        "de {month_name} del {year}",
        "correspondientes al mes de {month_name} del {year}",
        "registrados en el mes de {month_name} del {year}",
        "a lo largo del mes de {month_name} del {year}",
        "del periodo de {month_name} del {year}",
        "el mes de {month_name} del {year}",
        "mes de {month_name} del {year}",
        "en el mes del {year} correspondiente a {month_name}"
    ]

    chosen_variant = random.choice(variants)
    phrase = chosen_variant.format(month_name=meses_espanol[month-1], year=year)

    return phrase, {"startDate": start_date, "endDate": end_date}
