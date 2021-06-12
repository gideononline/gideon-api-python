import pandas as pd
from typing import Union

from gideon_api_python import gideon_api
from gideon_api_python.codes import lookup_item

ID_OR_STR = Union[int, str]


def outbreaks_by_year(year: int):
    return gideon_api.query_gideon_api('/diseases/outbreaks', {'year': year})


def outbreaks_by_country_year(country: ID_OR_STR, year: int):
    if isinstance(country, str):
        country = lookup_item('countries', country)
    return gideon_api.query_gideon_api(
        f'/diseases/outbreaks/distribution/{country}', {'year': year})


def latest_outbreaks_by_country(country: ID_OR_STR):
    if isinstance(country, str):
        country = lookup_item('countries', country)
    return gideon_api.query_gideon_api(
        f'/diseases/countries/{country}/latest-outbreaks')


def outbreaks_by_disease(disease: ID_OR_STR):
    if isinstance(disease, str):
        disease = lookup_item('diseases', disease)
    return gideon_api.query_gideon_api(f'/diseases/{disease}/outbreaks')


def endemic_countries_by_disease(disease: ID_OR_STR):
    if isinstance(disease, str):
        disease = lookup_item('diseases', disease)
    return gideon_api.query_gideon_api(f'/diseases/{disease}/countries')


def endemic_diseases_by_country(country: ID_OR_STR):
    if isinstance(country, str):
        country = lookup_item('countries', country)
    return gideon_api.query_gideon_api(f'/diseases/countries/{country}')
