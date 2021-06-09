_GENERAL_CATEGORIES = 'diseases', 'drugs', 'vaccines'
_MICROBIOLOGY_CATEGORIES = 'bacteria', 'mycobacteria', 'yeasts'
_COUNTRIES = 'countries'
_REGIONS = 'regions'
_ALL_CATEGORIES = (_GENERAL_CATEGORIES + _MICROBIOLOGY_CATEGORIES
                   + (_COUNTRIES, _REGIONS))


def get_endpoint(category: str) -> str:
    """Checks the category refering to a GIDEON API piece with a
        unique identifier. Allows for variation on spelling, such
        as disease vs diseases or country vs countries
    """
    category = category.strip().lower()

    # General categories are all spelled pluarl ending in an 's'
    general_keyword = category if category[-1] == 's' else f'{category}s'
    if general_keyword in _GENERAL_CATEGORIES:
        return f'/{general_keyword}'

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

    # Singular or pluarl spelling of regions
    if category in (_REGIONS[:-1], _REGIONS):
        return f'/travel/{_REGIONS}'

    raise ValueError(f'Category not one of {_ALL_CATEGORIES}')
