import random as rd
import json


def run():
    ind = dict()
    for qol in ['MAT_LIVING', 'HEALTH', 'EDUCATION', 'ECON_SAFETY',
                'LEISURE', 'GOVERN', 'LIVING_ENV', 'LIFE_EXP', 'EMPLOY']:
        ind[qol] = dict()
        for country in ['PL', 'DE', 'UK']:
            ind[qol][country] = dict()
            for year in ['2010', '2011', '2012', '2013', '2014', '2015']:
                ind[qol][country][year] = rd.uniform(-1.0, 1.0)
    result = dict()
    result['qualities'] = ind
    result = json.dumps(result)
    print(result)


if __name__ == '__main__':
    run()
