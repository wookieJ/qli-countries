from config import common


class Configuration:
    def __init__(self):
        self.HOST = 'host'
        self.LANG = 'language'
        self.FORMAT = 'format'

    @staticmethod
    def get_common(key):
        return common.EUROSTAT_COMMON_CONFIG[key]

    def get_host(self, key):
        host = self.get_common(self.HOST) + '/' + self.get_common(self.FORMAT) + '/' + \
               self.get_common(self.LANG) + '/' + key

        return host

    @staticmethod
    def apply_filters(url, dataset):
        if '?' not in url:
            url += '?'
        else:
            url += '&'
        for key in dataset.FILTERS:
            url += key + '=' + str(dataset.FILTERS[key]) + '&'
        url = url[0:-1]
        return url

    def get_url(self, dataset_code):
        module = None
        for qol_param in common.QOL_PARAMS:
            if dataset_code in common.QOL_PARAMS[qol_param]:
                module = common.QOL_PARAMS[qol_param][dataset_code]
                break

        url = self.get_host(dataset_code)
        url = self.apply_filters(url, common)
        if module is not None:
            url = self.apply_filters(url, module)

        return url
