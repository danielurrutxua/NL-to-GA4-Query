# app.py
import json
from modules.query_generators.query_builder import build_query


def main():
    num_pairs = 100
    pairs = []

    for _ in range(num_pairs):
        pair = build_query()
        pairs.append(pair)

    # Exportar los resultados a un archivo JSON
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(pairs, f, ensure_ascii=False, indent=4)
    print("Exportación a JSON completada.")


if __name__ == "__main__":
    main()
