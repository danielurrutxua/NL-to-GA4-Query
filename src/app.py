# app.py
import json
import pandas as pd
from modules.query_generators.query_builder import build_query


def main():
    num_pairs = 20
    pairs = []

    for _ in range(num_pairs):
        pair = build_query()
        pairs.append(pair)

    # Exportar los resultados a un archivo JSON
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(pairs, f, ensure_ascii=False, indent=4)
    print("Exportación a JSON completada.")

    # Cargar el archivo JSON
    with open("output.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Transformar los datos en un DataFrame
    rows = []
    for item in data:
        natural_language_query = item["natural_language_query"]
        api_query = json.dumps(item["api_query"], ensure_ascii=False)
        rows.append([natural_language_query, api_query])

    df = pd.DataFrame(rows, columns=["natural_language_query", "api_query"])

    # Exportar a CSV
    df.to_csv("output.csv", index=False, encoding="utf-8")
    print("Exportación a CSV completada.")


if __name__ == "__main__":
    main()
