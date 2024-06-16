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
