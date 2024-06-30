import pandas as pd

initial_phrases_df = pd.read_csv("resources/sinonimos_dime.csv")
metrics_df = pd.read_csv("resources/metrics.csv")
dimensions_df = pd.read_csv("resources/dimensions.csv")
english_words_df = pd.read_csv("resources/4000-most-common-english-words-csv.csv")


def get_random_initial_phrase():
    return initial_phrases_df.sample(n=1).iloc[0].iloc[0]


def get_random_metric():
    return metrics_df.sample(n=1).iloc[0]


def get_2_random_metrics():
    return metrics_df.sample(n=2).iloc[:2]


def get_random_dimension():
    return dimensions_df.sample(n=1).iloc[0]


def get_random_english_word():
    return english_words_df.sample(n=1).iloc[0]


def export_csv(pairs: list):
    rows = []
    for item in pairs:
        natural_language_query = item['natural_language_query']
        api_query = item['api_query']
        
        metrics = ";".join(api_query.get('metrics', []))
        dimensions = ";".join(api_query.get('dimensions', []))
        
        #date_ranges = api_query.get('dateRanges', [{}])[0]
        #start_date = date_ranges.get('startDate', "")
        #end_date = date_ranges.get('endDate', "")
        
        dimension_filter = ""
        if 'dimensionFilter' in api_query:
            filter_expression = api_query['dimensionFilter'].get('filter', {})
            field_name = filter_expression.get('fieldName', "")
            if 'stringFilter' in filter_expression:
                match_type = filter_expression['stringFilter'].get('matchType', "")
                value = filter_expression['stringFilter'].get('value', "")
                dimension_filter = f"{field_name};{match_type};{value}"
            elif 'numericFilter' in filter_expression:
                operation = filter_expression['numericFilter'].get('operation', "")
                value = filter_expression['numericFilter'].get('value', {}).get('int64Value', "")
                dimension_filter = f"{field_name};{operation};{value}"

        metric_filter = ""
        if 'metricFilter' in api_query:
            filter_expression = api_query['metricFilter'].get('filter', {})
            field_name = filter_expression.get('fieldName', "")
            if 'stringFilter' in filter_expression:
                match_type = filter_expression['stringFilter'].get('matchType', "")
                value = filter_expression['stringFilter'].get('value', "")
                metric_filter = f"{field_name};{match_type};{value}"
            elif 'numericFilter' in filter_expression:
                operation = filter_expression['numericFilter'].get('operation', "")
                value = filter_expression['numericFilter'].get('value', {}).get('int64Value', "")
                metric_filter = f"{field_name};{operation};{value}"
        
        #rows.append([natural_language_query, metrics, dimensions, start_date, end_date, dimension_filter, metric_filter])
        rows.append([natural_language_query, metrics, dimensions, dimension_filter, metric_filter])

    #df = pd.DataFrame(rows, columns=['natural_language_query', 'metrics', 'dimensions', 'start_date', 'end_date', 'dimensionFilter', 'metricFilter'])
    df = pd.DataFrame(rows, columns=['natural_language_query', 'metrics', 'dimensions', 'dimensionFilter', 'metricFilter'])

    df.to_csv('output.csv', index=False, encoding='utf-8')
    print("Exportación a CSV completada.")
def export_csv_compact(pairs: list):
    rows = []
    for item in pairs:
        natural_language_query = item['natural_language_query']
        api_query = item['api_query']
        
        metrics = ";".join(api_query.get('metrics', []))
        dimensions = ";".join(api_query.get('dimensions', []))
        
        date_ranges = api_query.get('dateRanges', [{}])[0]
        start_date = date_ranges.get('startDate', "")
        end_date = date_ranges.get('endDate', "")
        
        dimension_filter = ""
        if 'dimensionFilter' in api_query:
            filter_expression = api_query['dimensionFilter'].get('filter', {})
            field_name = filter_expression.get('fieldName', "")
            if 'stringFilter' in filter_expression:
                match_type = filter_expression['stringFilter'].get('matchType', "")
                value = filter_expression['stringFilter'].get('value', "")
                dimension_filter = f"{field_name};{match_type};{value}"
            elif 'numericFilter' in filter_expression:
                operation = filter_expression['numericFilter'].get('operation', "")
                value = filter_expression['numericFilter'].get('value', {}).get('int64Value', "")
                dimension_filter = f"{field_name};{operation};{value}"

        metric_filter = ""
        if 'metricFilter' in api_query:
            filter_expression = api_query['metricFilter'].get('filter', {})
            field_name = filter_expression.get('fieldName', "")
            if 'stringFilter' in filter_expression:
                match_type = filter_expression['stringFilter'].get('matchType', "")
                value = filter_expression['stringFilter'].get('value', "")
                metric_filter = f"{field_name};{match_type};{value}"
            elif 'numericFilter' in filter_expression:
                operation = filter_expression['numericFilter'].get('operation', "")
                value = filter_expression['numericFilter'].get('value', {}).get('int64Value', "")
                metric_filter = f"{field_name};{operation};{value}"
        
        target_parts = []
        if metrics:
            target_parts.append(f"m:{metrics}")
        if dimensions:
            target_parts.append(f"d:{dimensions}")
        if start_date and end_date:
            target_parts.append(f"s:{start_date}")
            target_parts.append(f"e:{end_date}")
        if dimension_filter:
            target_parts.append(f"df:{dimension_filter}")
        if metric_filter:
            target_parts.append(f"mf:{metric_filter}")
        
        target = " ".join(target_parts)
        
        rows.append([natural_language_query, target])

    df = pd.DataFrame(rows, columns=['natural_language_query', 'target'])

    df.to_csv('output_compact.csv', index=False, encoding='utf-8')
    print("Exportación a CSV compacta completada.")

def export_csv_compact_with_bars(pairs: list):
    rows = []
    for item in pairs:
        natural_language_query = item['natural_language_query']
        api_query = item['api_query']
        
        metrics = ";".join(api_query.get('metrics', []))
        dimensions = ";".join(api_query.get('dimensions', []))
        
        date_ranges = api_query.get('dateRanges', [{}])[0]
        start_date = date_ranges.get('startDate', "")
        end_date = date_ranges.get('endDate', "")
        
        dimension_filter = ""
        if 'dimensionFilter' in api_query:
            filter_expression = api_query['dimensionFilter'].get('filter', {})
            field_name = filter_expression.get('fieldName', "")
            if 'stringFilter' in filter_expression:
                match_type = filter_expression['stringFilter'].get('matchType', "")
                value = filter_expression['stringFilter'].get('value', "")
                dimension_filter = f"{field_name};{match_type};{value}"
            elif 'numericFilter' in filter_expression:
                operation = filter_expression['numericFilter'].get('operation', "")
                value = filter_expression['numericFilter'].get('value', {}).get('int64Value', "")
                dimension_filter = f"{field_name};{operation};{value}"

        metric_filter = ""
        if 'metricFilter' in api_query:
            filter_expression = api_query['metricFilter'].get('filter', {})
            field_name = filter_expression.get('fieldName', "")
            if 'stringFilter' in filter_expression:
                match_type = filter_expression['stringFilter'].get('matchType', "")
                value = filter_expression['stringFilter'].get('value', "")
                metric_filter = f"{field_name};{match_type};{value}"
            elif 'numericFilter' in filter_expression:
                operation = filter_expression['numericFilter'].get('operation', "")
                value = filter_expression['numericFilter'].get('value', {}).get('int64Value', "")
                metric_filter = f"{field_name};{operation};{value}"
        
        target_parts = [
            metrics if metrics else "",
            dimensions if dimensions else "",
            start_date if start_date else "",
            end_date if end_date else "",
            dimension_filter if dimension_filter else "",
            metric_filter if metric_filter else ""
        ]
        
        target = "|".join(target_parts)
        
        rows.append([natural_language_query, target])

    df = pd.DataFrame(rows, columns=['natural_language_query', 'target'])

    df.to_csv('output_compact.csv', index=False, encoding='utf-8')
    print("Exportación a CSV compacta completada.")
