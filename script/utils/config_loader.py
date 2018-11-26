from script.config import common


class Configuration:
    def __init__(self):
        self.HOST = 'host'
        self.LANG = 'language'
        self.FORMAT = 'format'

    @staticmethod
    def __get_common(attribute):
        """
        Getting attribute from common configuration file

        :param attribute: attribute name.
        :return: attribute value.
        """
        return common.API_COMMON_CONFIG[attribute]

    def __get_host(self, dataset_code):
        """
        Assemble url host. Format and language is defined in common configuration file

        :param dataset_code: name of database.
        :return: host main API url.
        """
        host = self.__get_common(self.HOST) + '/' + self.__get_common(self.FORMAT) + '/' + \
               self.__get_common(self.LANG) + '/' + dataset_code

        return host

    @staticmethod
    def __apply_filters(url, dataset_code):
        """
        Getting filters from configuration files of dataset code

        :param url: url on which we want to apply filters.
        :param dataset_code: name of database.
        :return:
        """
        if '?' not in url:
            url += '?'
        else:
            url += '&'
        for key in dataset_code.FILTERS:
            if isinstance(dataset_code.FILTERS[key], list):
                for value in dataset_code.FILTERS[key]:
                    url += key + '=' + str(value) + '&'
            else:
                url += key + '=' + str(dataset_code.FILTERS[key]) + '&'
        url = url[0:-1]
        return url

    def get_url(self, dataset_code):
        """
        Getting url to API based on common configuration file and data code filters

        :param dataset_code: name of database.
        :return: url with filetrs defined in configuration files.
        """
        module = None
        for qol_param in common.QOL_PARAMS:
            if dataset_code in common.QOL_PARAMS[qol_param]:
                module = common.QOL_PARAMS[qol_param][dataset_code]
                break

        url = self.__get_host(dataset_code)
        url = self.__apply_filters(url, common)
        if module is not None:
            url = self.__apply_filters(url, module)

        return url

    @staticmethod
    def get_params_list():
        """
        Getting parameters list from common configuration file

        :return: list with parameters list defined in common configuration file.
        """
        return common.QOL_PARAMS

    @staticmethod
    def get_subparams_list(param_name = None):
        """
        Getting sub parameters list from common configuration file

        :param param_name: parameter name.
        :return: list of sub parameters of this parameter, defined in common configuration file.
        """
        if param_name is not None:
            return common.QOL_PARAMS[param_name]
        else:
            return None

    @staticmethod
    def get_value(key):
        """
        Getting value of key in configuration file

        :param key: key of value we want to know
        :return: value of key in configuration file
        """
        for qol_param in common.QOL_PARAMS:
            if key in common.QOL_PARAMS[qol_param]:
                return common.QOL_PARAMS[qol_param][key]
