from script.utils.config_loader import Configuration
from script.utils.load import Loader
from script.utils.data_parse import parse_json


class Parameter:
    def __init__(self, name):
        self.name = name
        self.configuration = Configuration()
        self.loader = Loader()
        self.sub_params = []

    def load_sub_params(self):
        """
        Loading sub parameters of this parameter. Storing them into list as objects

        :return: nothing.
        """
        for param_name in self.configuration.get_params_list():
            if param_name is self.name:
                for sub_param in self.configuration.get_subparams_list(self.name):
                    url = self.configuration.get_url(sub_param)
                    data = self.loader.get_json(url)
                    self.sub_params.append(parse_json(data))
                break

    def print_sub_params_values(self, print_label=False):
        """
        Print values of sub parameters

        :return: nothing.
        """
        for sub_param in self.sub_params:
            if print_label:
                print(f'{sub_param["label"]}:')
            print(sub_param['value'])

    def get_values(self):
        """
        Get all parameter raw values

        :return: list of all parameter values
        """
        values = []
        for sub_param in self.sub_params:
            for value in sub_param['value']:
                values.append(sub_param['value'][value])
        return values
