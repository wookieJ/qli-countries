import random as rd
import json


def run():
    ind = dict()
    for country in ['AL', 'AM', 'AT', 'AZ', 'BE', 'BG', 'BY', 'CH', 'CY', 'CZ', 'DE', 'DK', 'EA18', 'EA19', 'EE',
                    'EEA30', 'EL', 'ES', 'EU27', 'EU28', 'FI', 'FR', 'FX', 'GE', 'HR', 'HU', 'IE', 'IS', 'IT', 'LI',
                    'LT', 'LU', 'LV', 'MD', 'ME', 'MK', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'RU', 'SE', 'SI',
                    'SK', 'SM', 'TR', 'UA', 'UK', 'XK', 'EA', 'EU']:
        ind[country] = dict()
        for qol in ['MAT_LIVING', 'HEALTH', 'EDUCATION', 'ECON_SAFETY',
                    'LEISURE', 'GOVERN', 'LIVING_ENV', 'LIFE_EXP', 'EMPLOY']:
            ind[country][qol] = [rd.uniform(0, 1.0) for i in range(2004, 2018)]
            if country is 'EU_AVG':
                ind[country][qol] = [rd.uniform(0, 1.0)] * (2018 - 2004)
        ind[country]['qol'] = rd.uniform(0, 1.0)
    result = dict()
    result['qualities'] = ind
    result = json.dumps(result)
    print(result)


if __name__ == '__main__':
    run()
