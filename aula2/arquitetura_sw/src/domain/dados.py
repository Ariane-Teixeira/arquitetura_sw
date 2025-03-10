import pandas as pd
import os

class Dados:
    def baixar_dataset(self, api, dataset_name):
        api.dataset_download_files(dataset_name, unzip=True, force=True)
        file_name = "postings.csv"
        return file_name

    def carregar_dados(self, file_name, max_rows=10000):
        df = pd.read_csv(file_name, nrows=max_rows)
        return df
    