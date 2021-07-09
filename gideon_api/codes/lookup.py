"""Look up the GIDEON API code for a particular item"""

from typing import Optional, Union
from gideon_api import gideon_api
from gideon_api.codes.categories import get_endpoint

ENDPOINT_ID_NAME = {
    '/diseases': ('disease_code', 'disease'),
    '/diseases/fingerprint/agents': ('agent_code', 'agent'),
    '/diseases/fingerprint/vectors': ('vector_code', 'vector'),
    '/diseases/fingerprint/vehicles': ('vehicle_code', 'vehicle'),
    '/diseases/fingerprint/reservoirs': ('reservoir_code', 'reservoir'),
    '/diseases/fingerprint/countries': ('country_code', 'country'),
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
            countries, etc. Refer to the :py:func:`gideon_api.get_endpoint`
            function documentation for a complete list.
        item:
            The name of the item, such as a particular disease or bacteria.

    Returns:
        If the item is found, the GIDEON API code
    """
    api_endpoint = get_endpoint(category)
    all_category_items = gideon_api.query_gideon_api(api_endpoint,
                                                     try_dataframe=False)

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
