"""
    File name: main.py
    Author: Łukasz Jędryczka
    Date created: 17/11/2018
    Python Version: 3.6
"""
from script.model.parameter import Parameter
from script.config import common
from script.utils.data_processing import linear_regression
import matplotlib.pyplot as plt
import numpy as np
import json

qualities = dict()


def merge_indicators(indicators):
    for geo in indicators:
        if geo not in qualities:
            qualities[geo] = dict()
        for qol in indicators[geo]:
            if qol not in qualities[geo]:
                qualities[geo][qol] = indicators[geo][qol]


def run():
    country = 'PL'
    countries = dict()

    for param_name in common.QOL_PARAMS:
        parameter = Parameter(param_name)
        parameter.load_sub_params()
        indicators = parameter.get_indicators(normalize=True, linearize=False)

        # getting countries list - remember to update common.py file
        for p in parameter.sub_params:
            for geo in p['dimension']['geo']['category']['label']:
                countries[geo] = p['dimension']['geo']['category']['label'][geo]

        linear_reg = linear_regression(indicators[country][param_name])

        plt.title(f'{param_name} in {country}')
        plt.plot(indicators['PL'][param_name])
        plt.plot(linear_reg)
        plt.xlabel('feature')
        plt.ylabel('value')
        years = [i for i in range(2004, 2018)]
        plt.xticks(np.arange(len(years)), years, rotation=70)
        plt.show()

        merge_indicators(indicators)

    print(countries)
    result = dict()
    result['qualities'] = qualities
    result['countries'] = common.COUNTRIES
    result = json.dumps(result)
    print(result)


if __name__ == '__main__':
    run()
