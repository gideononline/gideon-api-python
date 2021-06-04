import os.path
import pickle
from gideon_api_python.base import query_api

_LOOKUP_JSON = os.path.join(os.path.dirname(__file__), 'lookup.pickle')

_CATEGORIES = 'diseases', 'drugs', 'vaccines'
_MICROBIOLOGY_CATEGORIES = 'bacteria', 'mycobacteria', 'yeasts'
_TRAVEL_CATEGORIES = 'regions', 'countries'
_POSSIBLE_CATEGORIES = (_CATEGORIES + _MICROBIOLOGY_CATEGORIES
                        + _TRAVEL_CATEGORIES)


def check_category(keyword: str) -> str:
    """Checks the category refering to a GIDEON API piece with a
        unique identifier
    """
    keyword = keyword.strip().lower()
    # Check for countries
    if keyword in _CATEGORIES or keyword == _TRAVEL_CATEGORIES[1]:
        return f'/{keyword}'
    if keyword in _MICROBIOLOGY_CATEGORIES:
        return f'/microbiology/{keyword}'
    # Check for region
    if keyword == _TRAVEL_CATEGORIES[0]:
        return f'/travel/{_TRAVEL_CATEGORIES[0]}'
    raise ValueError(f'Category not one of {_POSSIBLE_CATEGORIES}')


# def check
