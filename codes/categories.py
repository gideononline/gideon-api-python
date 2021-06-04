import os.path
import pickle
from gideon_api_python.base import query_api

_LOOKUP_JSON = os.path.join(os.path.dirname(__file__), 'lookup.pickle')

_GENERAL_CATEGORIES = 'diseases', 'drugs', 'vaccines'
_MICROBIOLOGY_CATEGORIES = 'bacteria', 'mycobacteria', 'yeasts'
_COUNTRIES = 'countries'
_REGIONS = 'regions'
_ALL_CATEGORIES = (_GENERAL_CATEGORIES + _MICROBIOLOGY_CATEGORIES
                   + (_COUNTRIES, _REGIONS))


def check_category(keyword: str) -> str:
    """Checks the category refering to a GIDEON API piece with a
        unique identifier. Allows for variation on spelling, such
        as disease vs diseases or country vs countries
    """
    keyword = keyword.strip().lower()

    # General categories are all spelled pluarl ending in an 's'
    general_keyword = keyword if keyword[-1] == 's' else f'{keyword}s'
    if general_keyword in _GENERAL_CATEGORIES:
        return f'/{general_keyword}'

    microbiology_variations = {
        'bacterium': 'bacteria',
        'mycobacterium': 'mycobacteria',
        'yeast': 'yeasts',
    }
    # Try to convert spelling variation or just use original keyword
    microbio_keyword = microbiology_variations.get(keyword, keyword)
    if microbio_keyword in _MICROBIOLOGY_CATEGORIES:
        return f'/microbiology/{microbio_keyword}'

    if keyword in ('country', _COUNTRIES):
        return f'/{_COUNTRIES}'

    # Singular or pluarl spelling of regions
    if keyword in (_REGIONS[:-1], _REGIONS):
        return f'/travel/{_REGIONS}'

    raise ValueError(f'Category not one of {_ALL_CATEGORIES}')
