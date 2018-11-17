from utils.config_loader import Configuration
from utils.load import Loader
from utils.data_parse import parse_json


def run():
    configuration = Configuration()
    loader = Loader()
    url = configuration.get_url('demo_mlexpec')
    print(url)
    json = loader.get_json(url)
    life_expectancy = parse_json(json)
    print(life_expectancy)
    print(life_expectancy.get('value'))


if __name__ == '__main__':
    run()
