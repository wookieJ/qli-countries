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
                    print(f'Database: {self.configuration.get_value(sub_param)}, url: {url}')
                    self.sub_params.append(parse_json(data))
                break
        print()

    def print_sub_params_values(self, print_label=False):
        """
        Print values of sub parameters

        :return: nothing.
        """
        for sub_param in self.sub_params:
            if 'value' in sub_param:
                if print_label:
                    print(f'{sub_param["label"]}:')
                print(sub_param['value'])

    @staticmethod
    def __get_size(sub_param, key):
        """
        Get size of key value in object

        :param key: name of key value.
        :return: size of objects.
        """
        if 'id' in sub_param and 'size' in sub_param and key in sub_param['id']:
            return sub_param['size'][sub_param['id'].index(key)]
        else:
            return 0

    @staticmethod
    def __get_data_size(sub_param, key):
        """
        Get size of data

        :param key: name of key value.
        :return: size of objects.
        """
        if 'id' in sub_param and 'size' in sub_param and key in sub_param['id']:
            data_len = 1
            for i in range(sub_param['id'].index(key)):
                data_len *= sub_param['size'][i]
            return data_len
        else:
            return 0

    def __get_index(self, sub_param, year, geo):
        """
        Getting index of data in year and localization.
        :param sub_param: object od sub parameter.
        :param year: year we are interesting in.
        :param geo: location we are interesting in.
        :return: list
        """
        if 'dimension' in sub_param:
            year_index_list = sub_param['dimension']['time']['category']['index']
            geo_index_list = sub_param['dimension']['geo']['category']['index']
            if str(year) in year_index_list and geo in geo_index_list:
                data_idx_start = year_index_list[str(year)]
                geo_idx = geo_index_list[geo]
                year_data_size = self.__get_data_size(sub_param, 'time')
                geo_data_size = self.__get_data_size(sub_param, 'geo')
                year_size = self.__get_size(sub_param, 'time')
                geo_step = int(year_data_size / geo_data_size)
                data = [i for i in range(data_idx_start, data_idx_start + (year_data_size * year_size), year_size)]
                data = data[geo_idx::geo_step]
                return data
        return None

    def get_values(self, year, geo):
        """
        Get all parameter raw values

        :return: list of all parameter values
        """
        values = []
        for sub_param in self.sub_params:
            if 'value' in sub_param:
                data = self.__get_index(sub_param, year, geo)
                if data is not None:
                    for d in data:
                        if str(d) in sub_param['value']:
                            values.append(sub_param['value'][str(d)])
                        else:
                            values.append(':')
        return values
