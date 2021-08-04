"""Handles a mapping between category names and GIDEON API endpoints"""

_GENERAL_CATEGORIES = 'diseases', 'drugs', 'vaccines'
_FINGERPRINT_CATEGORIES = 'agents', 'vectors', 'vehicles', 'reservoirs'
_MICROBIOLOGY_CATEGORIES = 'bacteria', 'mycobacteria', 'yeasts'
_COUNTRIES = 'countries'
_REGIONS = 'regions'
_ALL_CATEGORIES = (_GENERAL_CATEGORIES + _MICROBIOLOGY_CATEGORIES +
                   (_COUNTRIES, _REGIONS))


def get_endpoint(category: str) -> str:
    """Checks the category refering to a GIDEON API piece with a
    unique identifier.

    Args:
        category: One of the following: 'diseases', 'drugs', 'vaccines',
            'agents', 'vectors', 'vehicles', 'reservoirs', 'bacteria',
            'mycobacteria', 'yeasts', 'countries', 'regions'

    Returns:
        A string representing the API endpoint for the particular category
        of items in the GIDEON API
    """
    category = category.strip().lower()

    # General categories are all spelled plural ending in an 's'
    general_keyword = category if category[-1] == 's' else f'{category}s'
    if general_keyword in _GENERAL_CATEGORIES:
        return f'/{general_keyword}'

    if category in _FINGERPRINT_CATEGORIES:
        return f'/diseases/fingerprint/{category}'

    microbiology_variations = {
        'bacterium': 'bacteria',
        'mycobacterium': 'mycobacteria',
        'yeast': 'yeasts',
    }
    # Try to convert spelling variation or just use original keyword
    microbio_keyword = microbiology_variations.get(category, category)
    if microbio_keyword in _MICROBIOLOGY_CATEGORIES:
        return f'/microbiology/{microbio_keyword}'

    if category in ('country', _COUNTRIES):
        return f'/{_COUNTRIES}'

    # Singular or plural spelling of regions
    if category in (_REGIONS[:-1], _REGIONS):
        return f'/travel/{_REGIONS}'

    raise ValueError(f'Category not one of {_ALL_CATEGORIES}')
