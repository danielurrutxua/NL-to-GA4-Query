import pandas as pd

metrics_df = pd.read_csv('resources/metrics.csv')
dimensions_df = pd.read_csv('resources/dimensions.csv')

def get_random_metric():
    return metrics_df.sample(n=1).iloc[0]

def get_random_dimension():
    return dimensions_df.sample(n=1).iloc[0]