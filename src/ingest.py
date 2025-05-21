import requests
import pandas as pd

def download_air_quality_csv(url, output_path):
    response = requests.get(url)
    with open(output_path, 'wb') as f:
        f.write(response.content)

def load_csv_to_df(path):
    return pd.read_csv(path, sep=';', decimal=',', na_values=-200)
