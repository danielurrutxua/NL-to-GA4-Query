import random
from ..constants.meses_espanol import meses_espanol

def generate_months_range(start_year, end_year, start_month, end_month):
    start_date = f"{start_year}-{start_month:02d}-01"
    if end_month == 1:  # Enero
        end_date = f"{end_year}-01-31"
    elif end_month == 2:  # Febrero
        if (end_year % 4 == 0 and end_year % 100 != 0) or (end_year % 400 == 0):
            end_date = f"{end_year}-02-29"  # Año bisiesto
        else:
            end_date = f"{end_year}-02-28"
    elif end_month == 3:  # Marzo
        end_date = f"{end_year}-03-31"
    elif end_month == 4:  # Abril
        end_date = f"{end_year}-04-30"
    elif end_month == 5:  # Mayo
        end_date = f"{end_year}-05-31"
    elif end_month == 6:  # Junio
        end_date = f"{end_year}-06-30"
    elif end_month == 7:  # Julio
        end_date = f"{end_year}-07-31"
    elif end_month == 8:  # Agosto
        end_date = f"{end_year}-08-31"
    elif end_month == 9:  # Septiembre
        end_date = f"{end_year}-09-30"
    elif end_month == 10:  # Octubre
        end_date = f"{end_year}-10-31"
    elif end_month == 11:  # Noviembre
        end_date = f"{end_year}-11-30"
    elif end_month == 12:  # Diciembre
        end_date = f"{end_year}-12-31"
    return start_date, end_date

def generate():
    start_year = random.randint(2000, 2024)
    end_year = random.randint(start_year, 2024)
    start_month = random.randint(1, 10)
    end_month = random.randint(start_month, 12)
    start_date, end_date = generate_months_range(start_year, end_year, start_month, end_month)

    variants = [
        "desde el mes de {start_month_name} de {start_year} hasta el mes de {end_month_name} de {end_year}",
        "del mes de {start_month_name} de {start_year} al mes de {end_month_name} de {end_year}",
        "entre el mes de {start_month_name} de {start_year} y el mes de {end_month_name} de {end_year}",
        "desde {start_month_name} de {start_year} hasta {end_month_name} de {end_year}",
        "desde {start_month_name} {start_year} hasta {end_month_name} {end_year}",
        "del periodo de {start_month_name} de {start_year} al periodo de {end_month_name} de {end_year}",
    ]

    variants_equal_year = [
        "desde {start_month_name} hasta {end_month_name} de {start_year}"
    ]

    chosen_variant = ""
    if start_year == end_year: chosen_variant = random.choice(variants_equal_year)
    else: chosen_variant = random.choice(variants)
    phrase = chosen_variant.format(start_month_name=meses_espanol[start_month-1], end_month_name=meses_espanol[end_month-1], start_year=start_year, end_year=end_year)

    return phrase, {"startDate": start_date, "endDate": end_date}