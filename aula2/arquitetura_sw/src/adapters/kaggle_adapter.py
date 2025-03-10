from kaggle.api.kaggle_api_extended import KaggleApi

class KaggleAdapter:
    def authenticate(self):
        api = KaggleApi()
        api.authenticate()
        return api