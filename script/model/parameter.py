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
from script.utils.data_processing import smooth_data
from script.utils.data_processing import linear_regression
import matplotlib.pyplot as plt
import numpy as np
import warnings
import copy


class Parameter:
    def __init__(self, name):
        self.name = name
        self.configuration = Configuration()
        self.loader = Loader()
        self.sub_params = []
        self.raw_data = None
        self.structured_data = None
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
                    data = parse_json(data)
                    data['data_length'] = self.configuration.get_value(sub_param).LENGTH
                    self.sub_params.append(data)
                break
        self.structured_data = self.get_structured_data()
        data_3d = []
        for key, value in self.structured_data.items():
            data_2d = [feature for year, feature in value.items()]
            data_3d.append(data_2d)
        data_3d = np.array(data_3d)
        self.raw_data = data_3d

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

    def get_structured_data(self):
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
                            cnt = 0
                            for d in data:
                                if geo not in values:
                                    values[geo] = dict()
                                if year not in values[geo]:
                                    values[geo][year] = []
                                if str(d) in sub_param['value']:
                                    app_value = sub_param['value'][str(d)]
                                    invert = self.configuration.get_value(sub_param['extension']['datasetId']).INVERT
                                    if invert and cnt % 10 in invert:
                                        app_value *= -1
                                    values[geo][year].append(app_value)
                                    cnt += 1
                                else:
                                    values[geo][year].append(np.NaN)
                t1, t2 = self.configuration.get_time_interval()[0], self.configuration.get_time_interval()[1]
                for geo in self.configuration.get_countries():
                    if geo not in values:
                        values[geo] = dict()
                    for year in range(t1, t2):
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

    def plot_feature(self, feature, country, title, print_all=True):
        """
        Get indicators matrix for parameter by years and geo

        :return: matrix of parameter values
        """
        if self.structured_data is not None:
            data = dict(self.structured_data)
        else:
            raise AttributeError('Not loaded data, run load_sub_params() method')

        number_of_features = self.configuration.get_number_of_features(self.name)

        if feature not in range(number_of_features):
            print(f'\nThere is no {feature} feature!')
            return
        if country not in data:
            print(f'\nThere is no {country} country!')
            return

        if self.raw_data is not None:
            data_3d = np.array(self.raw_data)
        else:
            raise AttributeError('Not loaded data, run load_sub_params() method')

        features = np.array([])
        for size in range(number_of_features):
            features = np.append(features, data_3d[:, :, size])
        features = np.array(features)

        if print_all:
            plt.plot(features)
            plt.title(f'{title} features')
            plt.xlabel('Number of data')
            plt.ylabel('Value')
            plt.show()

        features = np.array([])
        features = np.append(features, data_3d[:, :, feature])
        if print_all:
            plt.plot(features)
            plt.title(f'{feature} feature in all countries')
            plt.xlabel('Number of data')
            plt.ylabel('Value')
            plt.show()

        pl_index = list(data.keys()).index(country)
        start = pl_index * (self.configuration.get_time_interval()[1] - self.configuration.get_time_interval()[0])
        features = features[start:start+14]
        s_data, regression, r2, mean_fill, moving_average, moving_w_average = smooth_data(features, return_all=True)
        plt.plot(features)
        plt.plot(regression)
        years = data['PL'].keys()
        plt.title(f'Raw: {feature} feature in {country} - {title}, r2 = {format(r2, ".4f")}')
        plt.xticks(np.arange(len(years)), years, rotation=70)
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.show()

        plt.plot(s_data)
        plt.xticks(np.arange(len(years)), years, rotation=70)
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.title(f'Linear: {feature} feature in {country} - {title}')
        plt.show()

        plt.xticks(np.arange(len(years)), years, rotation=70)
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.title(f'Mean: {feature} feature in {country} - {title}')
        plt.plot(mean_fill)
        plt.show()

        plt.xticks(np.arange(len(years)), years, rotation=70)
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.title(f'Moving avg: {feature} feature in {country} - {title}')
        plt.plot(moving_average)
        plt.show()

        plt.xticks(np.arange(len(years)), years, rotation=70)
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.title(f'Moving W avg: {feature} feature in {country} - {title}')
        plt.plot(moving_w_average)
        plt.show()

    def get_indicators(self, normalize=True, linearize=False):
        """
        Get indicators matrix for parameter by years and geo

        :return: matrix of parameter values
        """
        if self.structured_data is not None:
            data = copy.deepcopy(self.structured_data)
        else:
            raise AttributeError('Not loaded data, run load_sub_params() method')

        if self.raw_data is not None:
            data_3d = np.array(self.raw_data)
        else:
            raise AttributeError('Not loaded data, run load_sub_params() method')

        number_of_features = self.configuration.get_number_of_features(self.name)
        features_min_maxes = dict()
        if normalize:
            for feature_idx in range(number_of_features):
                features = np.array(data_3d[:, :, feature_idx])
                features_min_maxes[feature_idx] = [9999, 0]
                for country_idx, country_feature in enumerate(features):
                    country_feature = smooth_data(country_feature)
                    min_val = country_feature.min()
                    max_val = country_feature.max()
                    if min_val < features_min_maxes[feature_idx][0]:
                        features_min_maxes[feature_idx][0] = min_val
                    if max_val > features_min_maxes[feature_idx][1]:
                        features_min_maxes[feature_idx][1] = max_val

        for feature_idx in range(number_of_features):
            features = np.array(data_3d[:, :, feature_idx])
            for country_idx, country_feature in enumerate(features):
                country_feature = smooth_data(country_feature)
                for year_feature_idx, year_feature in enumerate(country_feature):
                    geo_idx = list(data.keys())[country_idx]
                    year_idx = str(self.configuration.get_time_interval()[0] + year_feature_idx)
                    norm_value = year_feature
                    if normalize:
                        norm_value = year_feature - features_min_maxes[feature_idx][0]
                        norm_value /= (features_min_maxes[feature_idx][1] - features_min_maxes[feature_idx][0])
                    data[geo_idx][year_idx][feature_idx] = norm_value

        for geo in data:
            for year in data[geo]:
                data[geo][year] = sum(data[geo][year])

        indicators = dict()
        for geo in data:
            indicators[geo] = dict()
            indicators[geo][self.name] = []
            for year in data[geo]:
                indicators[geo][self.name].append(data[geo][year])
            if linearize:
                indicators[geo][self.name] = linear_regression(indicators[geo][self.name])

        return indicators
