from typing import Union
from gideon_api_python.codes import lookup_item


def outbreaks_by_year(gideon_api, year: int):
    return gideon_api.query_gideon_api('/diseases/outbreaks', {'year': year})


def outbreaks_by_country_year(gideon_api,
                              country: Union[str, int],
                              year: int):
    if isinstance(country, str):
        country = lookup_item(gideon_api, 'countries', country)
    return gideon_api.query_gideon_api(
        f'/diseases/outbreaks/distribution/{country}',
        {'year': year}
    )


def outbreaks_by_disease(gideon_api, disease: Union[str, int]):
    if isinstance(disease, str):
        disease = lookup_item(gideon_api, 'diseases', disease)
    return gideon_api.query_gideon_api(
        f'/diseases/{disease}/outbreaks'
    )


def endemic_countries_by_disease(gideon_api, disease: Union[str, int]):
    if isinstance(disease, str):
        disease = lookup_item(gideon_api, 'diseases', disease)
    return gideon_api.query_gideon_api(f'/diseases/{disease}/countries')
