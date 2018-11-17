import requests


class Loader:
    def get_data(self, url):
        return requests.get(url).content
