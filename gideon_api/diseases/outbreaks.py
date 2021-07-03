from gideon_api import gideon_api


def outbreaks_by_year(year: int):
    """Disease Outbreaks by Year

    `API reference for /diseases/outbreaks
    <https://api-doc.gideononline.com/#038e2b12-0b61-4432-a642-7192a64f8a5c>`_

    Args:
        year: 4 digit year.
    Returns:
        DataFrame: Returns a complete list of all outbreaks that occurred in a
        requested year for every country.
    """
    return gideon_api.query_gideon_api('/diseases/outbreaks', {'year': year})


def outbreaks_by_country_year(country_code: str, year: int):
    """Disease Outbreaks by Country and Year

    `API reference for /diseases/outbreaks/distribution/{country_code}
    <https://api-doc.gideononline.com/#16616aab-57f9-477d-b611-892b7f19cd43>`_

    Args:
        country_code: GIDEON country code
        year: 4 digit year.
    Returns:
        DataFrame: Returns complete list of all outbreaks that were reported in
        a requested country and year.
    """
    return gideon_api.query_gideon_api(
        f'/diseases/outbreaks/distribution/{country_code}', {'year': year})


def latest_outbreaks_by_country(country_code: str):
    """Latest Disease Outbreaks by Country

    `API reference for /diseases/countries/{country_code}/latest-outbreaks
    <https://api-doc.gideononline.com/#a331d79d-c265-48a3-a45a-dbca49c8d38d>`_

    Args:
        country_code: GIDEON country code
    Returns:
        DataFrame: Returns information of latest outbreak of every disease for a
        requested country.
    """
    return gideon_api.query_gideon_api(
        f'/diseases/countries/{country_code}/latest-outbreaks')


def outbreaks_by_disease(disease_code: int):
    """Countries with Specific Disease Outbreaks

    `API reference for /diseases/{disease_code}/outbreaks
    <https://api-doc.gideononline.com/#f1a87f41-a9a4-414a-b6f7-d15c1c8b9331>`_

    Args:
        disease_code: GIDEON disease code
    Returns:
        DataFrame: Returns list of all countries that have reported outbreaks of
        a disease.
    """
    return gideon_api.query_gideon_api(f'/diseases/{disease_code}/outbreaks')


def endemic_countries_by_disease(disease_code: int):
    """Endemic Countries of a Disease

    `API reference for /diseases/{disease_code}/countries
    <https://api-doc.gideononline.com/#20bc3345-8c15-4cc7-a6a3-24c8ac0ccf49>`_

    Args:
        disease_code: GIDEON disease code
    Returns:
        DataFrame: Returns list of all endemic countries of a disease.
    """
    return gideon_api.query_gideon_api(f'/diseases/{disease_code}/countries')


def endemic_diseases_by_country(country_code: int):
    """Diseases Endemic to a Country

    `API reference for /diseases/countries/{country_code}
    <https://api-doc.gideononline.com/#feab6f00-e926-49df-9a34-114cfafdf685>`_

    Args:
        country_code: GIDEON country code
    Returns:
        DataFrame: Returns the list of all diseases that are endemic to the
        country.
    """
    return gideon_api.query_gideon_api(f'/diseases/countries/{country_code}')
