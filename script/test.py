#!/usr/bin/python
# -*- coding: utf-8 -*-
import random as rd
import json

COUNTRIES = {
    'AL': 'Albania',
    'AM': 'Armenia',
    'AT': 'Austria',
    'AZ': 'Azerbaijan',
    'BE': 'Belgium',
    'BG': 'Bulgaria',
    'BY': 'Belarus',
    'CH': 'Switzerland',
    'CY': 'Cyprus',
    'CZ': 'Czechia',
    'DE': 'Germany (until 1990 former territory of the FRG)',
    'DE_TOT': 'Germany including former GDR',
    'DK': 'Denmark',
    'EA18': 'Euro area (18 countries)',
    'EA19': 'Euro area (19 countries)',
    'EE': 'Estonia',
    'EEA30': 'European Economic Area (EU27 -  before the accession of Croatia, plus IS, LI, NO)',
    'EEA31': 'European Economic Area (EU28  - current composition, plus IS, LI, NO)',
    'EFTA': 'European Free Trade Association',
    'EL': 'Greece',
    'ES': 'Spain',
    'EU27': 'European Union (before the accession of Croatia)',
    'EU28': 'European Union (current composition)',
    'FI': 'Finland',
    'FR': 'France',
    'FX': 'France (metropolitan)',
    'GE': 'Georgia',
    'HR': 'Croatia',
    'HU': 'Hungary',
    'IE': 'Ireland',
    'IS': 'Iceland',
    'IT': 'Italy',
    'LI': 'Liechtenstein',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'LV': 'Latvia',
    'MD': 'Moldova',
    'ME': 'Montenegro',
    'MK': 'Former Yugoslav Republic of Macedonia, the',
    'MT': 'Malta',
    'NL': 'Netherlands',
    'NO': 'Norway',
    'PL': 'Poland',
    'PT': 'Portugal',
    'RO': 'Romania',
    'RS': 'Serbia',
    'RU': 'Russia',
    'SE': 'Sweden',
    'SI': 'Slovenia',
    'SK': 'Slovakia',
    'SM': 'San Marino',
    'TR': 'Turkey',
    'UA': 'Ukraine',
    'UK': 'United Kingdom',
    'XK': 'Kosovo (under United Nations Security Council Resolution 1244/99)',
    'EA': 'Euro area',
    'EU': 'European Union',
    'EU_AVG': 'European average value'
}


def run():
    ind = dict()
    for country in ['AL', 'AM', 'AT', 'AZ', 'BE', 'BG', 'BY', 'CH', 'CY', 'CZ', 'DE', 'DK', 'EA18', 'EA19', 'EE',
                    'EEA30', 'EL', 'ES', 'EU27', 'EU28', 'FI', 'FR', 'FX', 'GE', 'HR', 'HU', 'IE', 'IS', 'IT', 'LI',
                    'LT', 'LU', 'LV', 'MD', 'ME', 'MK', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'RU', 'SE', 'SI',
                    'SK', 'SM', 'TR', 'UA', 'UK', 'XK', 'EA', 'EU', 'EU_AVG']:
        ind[country] = dict()
        for qol in ['MAT_LIVING', 'HEALTH', 'EDUCATION', 'ECON_SAFETY',
                    'LEISURE', 'GOVERN', 'LIVING_ENV', 'LIFE_EXP', 'EMPLOY']:
            ind[country][qol] = [rd.uniform(0, 1.0) for i in range(2004, 2018)]
            if country is 'EU_AVG':
                ind[country][qol] = [rd.uniform(0, 1.0)] * (2018 - 2004)
        ind[country]['qol'] = [rd.uniform(0, 1.0) for i in range(2004, 2018)]
    result = dict()
    result['qualities'] = ind
    result['countries'] = COUNTRIES
    result = json.dumps(result)
    print(result)


if __name__ == '__main__':
    run()
