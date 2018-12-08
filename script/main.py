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


def run():
    param_name = common.HEALTH
    parameter = Parameter(param_name)
    parameter.load_sub_params()
    parameter.print_sub_params_values(print_label=True)
    parameter.plot_feature(0, 'PL', param_name, print_all=False)
    indicators = parameter.get_indicators(normalize=True)

    country = 'PL'
    print(indicators[country][param_name])
    linear_reg = linear_regression(indicators[country][param_name])

    plt.title(f'{param_name} in {country}')
    plt.plot(indicators[country][param_name])
    plt.plot(linear_reg)
    plt.xlabel('feature')
    plt.ylabel('value')
    years = [i for i in range(2004, 2018)]
    plt.xticks(np.arange(len(years)), years, rotation=70)
    plt.show()


if __name__ == '__main__':
    run()
