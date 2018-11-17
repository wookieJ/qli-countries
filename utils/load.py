import requests


class Loader:
    @staticmethod
    def get_json(url):
        return requests.get(url).content
