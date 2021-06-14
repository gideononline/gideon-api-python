from gideon_api_python import gideon_api, CODE_OR_NAME
from gideon_api_python.codes import lookup_item


def outbreaks_by_year(year: int):
    """https://api-doc.gideononline.com/#038e2b12-0b61-4432-a642-7192a64f8a5c"""
    return gideon_api.query_gideon_api('/diseases/outbreaks', {'year': year})


def outbreaks_by_country_year(country: CODE_OR_NAME, year: int):
    """https://api-doc.gideononline.com/#16616aab-57f9-477d-b611-892b7f19cd43"""
    if isinstance(country, str):
        country = lookup_item('countries', country)
    return gideon_api.query_gideon_api(
        f'/diseases/outbreaks/distribution/{country}', {'year': year})


def latest_outbreaks_by_country(country: CODE_OR_NAME):
    """https://api-doc.gideononline.com/#a331d79d-c265-48a3-a45a-dbca49c8d38d"""
    if isinstance(country, str):
        country = lookup_item('countries', country)
    return gideon_api.query_gideon_api(
        f'/diseases/countries/{country}/latest-outbreaks')


def outbreaks_by_disease(disease: CODE_OR_NAME):
    """https://api-doc.gideononline.com/#f1a87f41-a9a4-414a-b6f7-d15c1c8b9331"""
    if isinstance(disease, str):
        disease = lookup_item('diseases', disease)
    return gideon_api.query_gideon_api(f'/diseases/{disease}/outbreaks')


def endemic_countries_by_disease(disease: CODE_OR_NAME):
    """https://api-doc.gideononline.com/#20bc3345-8c15-4cc7-a6a3-24c8ac0ccf49"""
    if isinstance(disease, str):
        disease = lookup_item('diseases', disease)
    return gideon_api.query_gideon_api(f'/diseases/{disease}/countries')


def endemic_diseases_by_country(country: CODE_OR_NAME):
    """https://api-doc.gideononline.com/#feab6f00-e926-49df-9a34-114cfafdf685"""
    if isinstance(country, str):
        country = lookup_item('countries', country)
    return gideon_api.query_gideon_api(f'/diseases/countries/{country}')
