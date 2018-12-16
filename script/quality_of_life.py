"""
    File name: quality_of_life.py
    Author: Łukasz Jędryczka
    Date created: 17/11/2018
    Python Version: 3.6
"""
from script.model.parameter import Parameter
from script.config import common
from script.utils.data_processing import linear_regression
import matplotlib.pyplot as plt
import json

qualities = dict()


def run():
    """
    Main algorithm which gathering indicators of each parameters and merging them into one response
    :return:
    """
    country = 'PL'
    countries = dict()
    years = [i for i in range(2004, 2018)]

    for param_name in common.QOL_PARAMS:
        parameter = Parameter(param_name)
        parameter.load_sub_params()
        indicators = parameter.get_indicators(normalize=True, linearize=False)

        # getting countries list - remember to update common.py file
        for p in parameter.sub_params:
            for geo in p['dimension']['geo']['category']['label']:
                countries[geo] = p['dimension']['geo']['category']['label'][geo]

        linear_reg = linear_regression(indicators[country][param_name])
        # plt.plot(indicators['PL'][param_name])
        # parameter.plot_feature(linear_reg, years, f'{param_name} in {country}')
        __merge_indicators(indicators)

    __add_qol_indicators()
    # for country in common.COUNTRIES:
    #     Parameter.plot_feature(qualities[country]['qol'], years, f'Quality of life in {common.COUNTRIES[country]}')

    print(countries)
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
