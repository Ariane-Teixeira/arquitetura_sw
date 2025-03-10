from kaggle.api.kaggle_api_extended import KaggleApi

class Autenticacao:
    def autenticar_kaggle(self):
        api = KaggleApi()
        api.authenticate()
        return api