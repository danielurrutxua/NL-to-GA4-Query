import pandas as pd

def export(pairs):
    data = []
    for pair in pairs:
        natural_language_query = pair[0]
        api_query = pair[1]
        metrics = ', '.join(api_query['metrics'])
        date_ranges = ', '.join([f"{date_range['startDate']} to {date_range['endDate']}" for date_range in api_query['dateRanges']])
        data.append({'Natural Language Query': natural_language_query, 'Metrics': metrics, 'Date Ranges': date_ranges})

    # Crear el DataFrame
    df = pd.DataFrame(data)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv('lenguaje_natural_to_ga4_api_query.csv', index=False)

    # Mostrar las primeras filas del DataFrame
    print(df.head(100))
