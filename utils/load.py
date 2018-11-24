import requests


class Loader:
    @staticmethod
    def get_json(url):
        """
        Make a GET request on url

        :param url: url to which we are requesting.
        :return: returned response body
        """
        return requests.get(url).content
