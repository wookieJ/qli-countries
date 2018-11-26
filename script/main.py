from script.model.parameter import Parameter
from script.config import common


def run():
    parameter = Parameter(common.HEALTH)
    parameter.load_sub_params()
    parameter.print_sub_params_values(print_label=True)
    country = 'PL'
    for year in range (1990, 2019):
        print(f'\nHealth features for {country} in {year}:')
        data = parameter.get_values(year, country)
        print(f'{data}, len = {len(data)}')


if __name__ == '__main__':
    run()
