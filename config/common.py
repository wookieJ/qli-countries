from config.health import life_expectancy
from config.health import healthy_life_years
from config.health import unmet_medical_exams
from config.education import teritiary_education_level
from config.education import participation_rate_in_education
from config.education import early_leavers_from_education
from config.material import mean_median_net_income
from config.material import gross_domestic_product
from config.material import leaking_roof_population
from config.material import poverty_risk

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
        'demo_mlexpec': life_expectancy,
        'hlth_hlye': healthy_life_years,
        'hlth_silc_14': unmet_medical_exams
    },
    'education': {
        'edat_lfse_03': teritiary_education_level,
        'trng_lfs_02': participation_rate_in_education,
        'edat_lfse_14': early_leavers_from_education
    },
    'material_living_conditions': {
        'ilc_di03': mean_median_net_income,
        'nama_10_pc': gross_domestic_product,
        'ilc_mdho01': leaking_roof_population,
        'ilc_li02': poverty_risk
    }
}
