import json


def parse_json(data):
    """
    Parsing json into python object

    :param data: data we want to parse.
    :return: parsed data.
    """
    return json.loads(data)
