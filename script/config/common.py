"""
    File name: common.py
    Author: Łukasz Jędryczka
    Date created: 17/11/2018
    Python Version: 3.6

    Common configurations attributes for API datasets.
"""
from script.config.health import life_expectancy, unmet_medical_exams, healthy_life_years
from script.config.education import participation_rate_in_education, early_leavers_from_education, \
    teritiary_education_level
from script.config.material import mean_median_net_income, leaking_roof_population, poverty_risk, gross_domestic_product

API_COMMON_CONFIG = {
    'host': 'http://ec.europa.eu/eurostat/wdds/rest/data/v2.1',
    'language': 'en',
    'format': 'json'
}

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
    'EU': 'European Union'
}

SEX = {
    'female': 'F',
    'male': 'M',
    'total': 'T'
}

TIME_INTERVAL = 2004, 2018

FILTERS = {
    'sinceTimePeriod': 2004,
    'precision': 1,
    'sex': SEX['total'],
    'geo': list(COUNTRIES.keys())
}

HEALTH = 'health'
EDUCATION = 'education'
MATERIAL_CONDITIONS = 'material_living_conditions'

QOL_PARAMS = {
    HEALTH: {
        'demo_mlexpec': life_expectancy,
        'hlth_hlye': healthy_life_years,
        'hlth_silc_14': unmet_medical_exams
    },
    EDUCATION: {
        'edat_lfse_03': teritiary_education_level,
        'trng_lfs_02': participation_rate_in_education,
        'edat_lfse_14': early_leavers_from_education
    },
    MATERIAL_CONDITIONS: {
        'ilc_di03': mean_median_net_income,
        'nama_10_pc': gross_domestic_product,
        'ilc_mdho01': leaking_roof_population,
        'ilc_li02': poverty_risk
    }
}
