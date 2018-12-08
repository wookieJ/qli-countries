"""
    File name: main.py
    Author: Łukasz Jędryczka
    Date created: 17/11/2018
    Python Version: 3.6
"""
from script.model.parameter import Parameter
from script.config import common
import matplotlib.pyplot as plt


def run():
    param_name = common.HEALTH
    parameter = Parameter(param_name)
    parameter.load_sub_params()
    parameter.print_sub_params_values(print_label=True)
    parameter.plot_feature(0, 'PL', param_name, print_all=False)
    indicators = parameter.get_indicators()
    data_3d = []
    for key, value in indicators.items():
        data_2d = [feature for year, feature in value.items()]
        data_3d.append(data_2d)

    country = 'PL'
    year = '2007'

    plt.title(f'{param_name} in {country} in {year}')
    plt.plot(indicators[country][year])
    plt.xlabel('feature')
    plt.ylabel('value')
    plt.show()


if __name__ == '__main__':
    run()
