"""
    File name: main.py
    Author: Łukasz Jędryczka
    Date created: 17/11/2018
    Python Version: 3.6

    Getting data from API. Making the requests.
"""
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
