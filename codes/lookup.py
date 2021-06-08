"""Interfaces with the GIDEON disease list"""

from typing import Optional, Union
from gideon_api_python.base import query_gideon_api
from gideon_api_python.codes.categories import get_endpoint

PATH_DISEASE = '/diseases'

_CACHED_DISEASE_LIST = None



# def fetch_diseases(try_cached: bool = True):
#     """Fetches the disease list from GIDEON API

#     The disease list could be retrived from the API online or use
#     a recently saved cached version.

#     Args:
#         try_cached: Try to lookup the diease list locally first, before
#             checking the online version.

#     Returns:
#         A list of diseases where each entry is a dictonary.
#     """
#     global _CACHED_DISEASE_LIST
#     if _CACHED_DISEASE_LIST is None or not try_cached:
#         _CACHED_DISEASE_LIST = api_query(PATH_DISEASE)['data']
#     return _CACHED_DISEASE_LIST


# def get_disease_code_from_name(
#     search_name: str, strict_match: bool = False
# ) -> Optional[bool]:
#     """Lookup GIDEON disease code from a disease name

#     The disease code is necessary to access disease specifics from
#     the GIDEON API.

#     Args:
#         seach_name: The name of the disease to search. The search is case
#             insensitive.

#     Returns:
#         If a disease can be unambiguously determined, a number.
#     """
#     #TODO consider adding the option of a strict name search
#     # Do all searches in lower case
#     search_name = search_name.lower()
#     possible_diseases = []
#     for disease in fetch_diseases():
#         if search_name in disease['disease'].lower():
#             possible_diseases.append(disease)

#     # This is currently a two step process of trying to determine correct
#     # disease code from search_name.
#     # Try to filter diseases if the search has multiple possibilities.
#     # If there are multiple options, either return false for strict matching
#     # or further filter the possible list by an exact (case insensitive) match

#     #TODO reduce code duplication and implement strict matching logic

#     if not possible_diseases:  # No diseases were matched
#         return None
#     if len(possible_diseases) == 1:
#         return possible_diseases[0]['disease_code']

#     # Try to narrow down possible diseases from options
#     if not strict_match:
#         possible_diseases = [
#             x for x in possible_diseases
#             if search_name == x['disease_name'].lower()
#         ]
#         if not possible_diseases:  # No diseases were matched
#             return None
#         if len(possible_diseases) == 1:
#             return possible_diseases[0]['disease_code']

ENDPOINT_ID_NAME = {
    '/diseases': ('disease_code', 'disease'),
    '/drugs': ('drug_code', 'drug'),
    '/vaccines': ('vaccine_code', 'vaccine'),
    '/microbiology/bacteria': ('bacteria_code', 'bacteria'),
    '/microbiology/mycobacteria': ('mycobacteria_code', 'mycobacteria'),
    '/microbiology/yeasts': ('yeast_code', 'yeast'),
    '/countries': ('country_code', 'country'),
    '/travel/regions': ('region_code', 'region'),
}


def lookup_item(category: str, item: str) -> Optional[Union[int, str]]:
    """Looks up the GIDEON ID for a particular item.

    Args:
        category: The GIDEON API to search from such as diseases, vaccines,
            countries, etc.
        item:
            The name of the item, such as a particular disease or bacteria.

    Returns:
        If the item is found, the GIDEON API code
    """
    api_endpoint = get_endpoint(category)
    all_category_items = query_gideon_api(api_endpoint)

    # All items should be under the 'data' key
    assert 'data' in all_category_items

    # Check for item, expects exact match for now
    search_name = item.strip().lower()
    possible_matches = []

    id_key, name_key = ENDPOINT_ID_NAME[api_endpoint]
    for catalog_item in all_category_items['data']:
        id_ = catalog_item[id_key]
        name = catalog_item[name_key]

        if name.strip().lower() == search_name:
            possible_matches.append((id_, name))
    
    # Ensure only one option matched
    if len(possible_matches) == 1:
        return possible_matches[0][0]
    
    # Show multiple matches otherwise
    if len(possible_matches) > 1:
        return possible_matches
