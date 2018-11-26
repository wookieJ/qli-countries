from script.config.health import life_expectancy, unmet_medical_exams, healthy_life_years
from script.config.education import participation_rate_in_education, early_leavers_from_education, \
    teritiary_education_level
from script.config.material import mean_median_net_income, leaking_roof_population, poverty_risk, gross_domestic_product

API_COMMON_CONFIG = {
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
    # 'sinceTimePeriod': 2004,
    'precision': 1,
    'sex': SEX['total']
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
