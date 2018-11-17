from config.health import life_expectancy

EUROSTAT_COMMON_CONFIG = {
    'host': 'http://ec.europa.eu/eurostat/wdds/rest/data/v2.1',
    'language': 'en',
    'format': 'json'
}

COUNTRIES = [
    'PL', 'UK'
]

SEX = {
    'female': 'F',
    'male': 'M',
    'total': 'T'
}

FILTERS = {
    'sinceTimePeriod': 2004,
    'precision': 1,
    'sex': SEX['total']
}

QOL_PARAMS = {
    'health': {
        'demo_mlexpec': life_expectancy
    }
}
