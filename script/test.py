import random as rd
import json


def run():
    ind = dict()
    for country in ['PL', 'DE', 'UK', 'EU_AVG']:
        ind[country] = dict()
        for qol in ['MAT_LIVING', 'HEALTH', 'EDUCATION', 'ECON_SAFETY',
                    'LEISURE', 'GOVERN', 'LIVING_ENV', 'LIFE_EXP', 'EMPLOY']:
            ind[country][qol] = [rd.uniform(0, 1.0) for i in range(2004, 2018)]
            if country is 'EU_AVG':
                ind[country][qol] = [rd.uniform(0, 1.0)] * (2018 - 2004)
    result = dict()
    result['qualities'] = ind
    result = json.dumps(result)
    print(result)


if __name__ == '__main__':
    run()
