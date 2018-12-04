"""
    File name: main.py
    Author: Łukasz Jędryczka
    Date created: 17/11/2018
    Python Version: 3.6
"""
from script.model.parameter import Parameter
from script.config import common


def run():
    parameter = Parameter(common.EDUCATION)
    parameter.load_sub_params()
    parameter.print_sub_params_values(print_label=True)
    parameter.plot_feature(0, 'PL')


if __name__ == '__main__':
    run()
