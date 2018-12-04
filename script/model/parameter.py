"""
    File name: parameter.py
    Author: Łukasz Jędryczka
    Date created: 24/11/2018
    Python Version: 3.6

    Parameter class and their methods. Retrieving data from API and computing data.
"""
from script.utils.config_loader import Configuration
from script.utils.load import Loader
from script.utils.data_parse import parse_json
import matplotlib.pyplot as plt
import numpy as np
import warnings


class Parameter:
    def __init__(self, name):
        self.name = name
        self.configuration = Configuration()
        self.loader = Loader()
        self.sub_params = []
        warnings.simplefilter(action='ignore', category=FutureWarning)

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
                    data = parse_json(data)
                    data['data_length'] = self.configuration.get_value(sub_param).LENGTH
                    self.sub_params.append(data)
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

    def get_raw_values(self):
        """
        Get all parameter raw values

        :return: list of all sub parameter values
        """
        values = dict()
        size = 0
        for sub_param in self.sub_params:
            if 'value' in sub_param:
                for geo in sub_param['dimension']['geo']['category']['label']:
                    for year in sub_param['dimension']['time']['category']['label']:
                        data = self.__get_index(sub_param, year, geo)
                        if data is not None:
                            for d in data:
                                if geo not in values:
                                    values[geo] = dict()
                                if year not in values[geo]:
                                    values[geo][year] = []
                                if str(d) in sub_param['value']:
                                    values[geo][year].append(sub_param['value'][str(d)])
                                else:
                                    values[geo][year].append(np.NaN)
                for geo in self.configuration.get_countries():
                    if geo not in values:
                        values[geo] = dict()
                    for year in range(self.configuration.get_time_interval()[0], self.configuration.get_time_interval()[1]):
                        year = str(year)
                        if year not in values[geo]:
                            values[geo][year] = []
                        value = values[geo][year]
                        for i in range(sub_param['data_length'] + size - len(value)):
                            values[geo][year].append(np.NaN)
                size += sub_param['data_length']

            else:
                raise AttributeError
        return values

    def plot_feature(self, feature, country):
        """
        Get indicators matrix for parameter by years and geo

        :return: matrix of parameter values
        """
        data = self.get_raw_values()
        number_of_features = self.configuration.get_number_of_features(self.name)
        if feature not in  range(number_of_features):
            print(f'\nThere is no {feature} feature!')
            return
        if country not in data:
            print(f'\nThere are no {country} country!')
            return

        # Parsing data to 3D array
        data_3d = []
        for key, value in data.items():
            data_2d = [feature for year, feature in value.items()]
            data_3d.append(data_2d)

        data_3d = np.array(data_3d)

        features = np.array([])
        for size in range(number_of_features):
            features = np.append(features, data_3d[:, :, size])
        features = np.array(features)
        features.flatten()
        plt.plot(features)
        plt.title('Educational features')
        plt.xlabel('Number of data')
        plt.ylabel('Value')
        plt.show()

        features = np.array([])
        features = np.append(features, data_3d[:, :, feature])
        features = np.array(features)
        features.flatten()
        plt.plot(features)
        plt.title(f'{feature} feature in all countries')
        plt.xlabel('Number of data')
        plt.ylabel('Value')
        plt.show()

        pl_index = list(data.keys()).index(country)
        start = pl_index * (self.configuration.get_time_interval()[1] - self.configuration.get_time_interval()[0])
        features = features[start:start+14]
        plt.plot(features)
        years = data['PL'].keys()
        plt.xticks(np.arange(len(years)), years, rotation=70)
        plt.title(f'{feature} feature in {country}')
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.show()

    def get_indicators(self):
        """
        Get indicators matrix for parameter by years and geo

        :return: matrix of parameter values
        """
        # normalization
        # data[geo][year] = ((value - x_min) / (x_max - x_min) - 0.5) * 2
        return 0
