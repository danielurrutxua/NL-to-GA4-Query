# app.py
import json
import pandas as pd
from modules.query_generators.query_builder import build_query


def main():
    num_pairs = 100
    pairs = []

    for _ in range(num_pairs):
        pair = build_query()
        pairs.append(pair)

    # Transformar los datos en un DataFrame
    rows = []
    for item in pairs:
        natural_language_query = item['natural_language_query']
        api_query = item['api_query']
        
        metrics = ";".join(api_query.get('metrics', []))
        dimensions = ";".join(api_query.get('dimensions', []))
        
        # Asumimos que solo hay un rango de fechas por simplicidad
        date_ranges = api_query.get('dateRanges', [{}])[0]
        start_date = date_ranges.get('startDate', "")
        end_date = date_ranges.get('endDate', "")
        
        dimension_filter = json.dumps(api_query.get('dimensionFilter', {}), ensure_ascii=False) if 'dimensionFilter' in api_query else ""
        metric_filter = json.dumps(api_query.get('metricFilter', {}), ensure_ascii=False) if 'metricFilter' in api_query else ""
        
        rows.append([natural_language_query, metrics, dimensions, start_date, end_date, dimension_filter, metric_filter])

    df = pd.DataFrame(rows, columns=['natural_language_query', 'metrics', 'dimensions', 'start_date', 'end_date', 'dimensionFilter', 'metricFilter'])

    # Exportar a CSV
    df.to_csv('output.csv', index=False, encoding='utf-8')
    print("Exportación a CSV completada.")


if __name__ == "__main__":
    main()
