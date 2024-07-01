# app.py
from modules.query_generators.query_builder import build_query
from modules.utils.resources import export_csv
from modules.utils.resources import export_csv_compact


def main():
    num_pairs = 500000
    pairs = []

    for _ in range(num_pairs):
        pair = build_query()
        pairs.append(pair)

    export_csv(pairs)
    export_csv_compact(pairs)


if __name__ == "__main__":
    main()
