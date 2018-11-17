from utils.config_loader import Configuration
from utils.load import Loader


def run():
    configuration = Configuration()
    loader = Loader()
    print(loader.get_data(configuration.get_url('demo_mlexpec')))


if __name__ == '__main__':
    run()
