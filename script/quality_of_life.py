# coding=utf-8
"""
    File name: quality_of_life.py
    Author: Łukasz Jędryczka
    Date created: 17/11/2018
    Python Version: 3.6
"""
from model.parameter import Parameter
from config import common
import json

qualities = dict()


def run():
    """
    Main algorithm which gathering indicators of each parameters and merging them into one response
    :return:
    """
    countries = dict()

    for param_name in common.QOL_PARAMS:
        parameter = Parameter(param_name)
        parameter.load_sub_params()
        indicators = parameter.get_indicators(normalize=True, linearize=False)

        # getting countries list - remember to update common.py file
        for p in parameter.sub_params:
            for geo in p['dimension']['geo']['category']['label']:
                countries[geo] = p['dimension']['geo']['category']['label'][geo]

        __merge_indicators(indicators)

    __add_qol_indicators()
    __return_to_stdout()


def __merge_indicators(indicators):
    """
    Merging indicators from parameter into one response
    :param indicators: indicators from one parameter
    :return:
    """
    for geo in indicators:
        if geo not in qualities:
            qualities[geo] = dict()
        for qol in indicators[geo]:
            if qol not in qualities[geo]:
                qualities[geo][qol] = indicators[geo][qol]


def __return_to_stdout():
    """
    Printing final response in json format to stdout
    :return:
    """
    result = dict()
    result['qualities'] = qualities
    result['countries'] = common.COUNTRIES
    result = json.dumps(result)
    print(result)


def __add_qol_indicators():
    """
    Add to ind_np final quality of life indicator of each country
    :return: quality of life indicators
    """
    time_interval = common.TIME_INTERVAL[1] - common.TIME_INTERVAL[0]
    for geo in qualities:
        qualities[geo]['qol'] = []
        for year in range(time_interval):
            indicator = 0
            for qol in qualities[geo]:
                if qol is not 'qol':
                    indicator += qualities[geo][qol][year]
            qualities[geo]['qol'].append(indicator)


if __name__ == '__main__':
    run()
