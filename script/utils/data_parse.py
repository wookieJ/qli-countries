"""
    File name: main.py
    Author: Łukasz Jędryczka
    Date created: 17/11/2018
    Python Version: 3.6

    Parsing data.
"""
import json


def parse_json(data):
    """
    Parsing json into python object

    :param data: data we want to parse.
    :return: parsed data.
    """
    return json.loads(data)
