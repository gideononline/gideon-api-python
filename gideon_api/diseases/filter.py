from typing import Optional
from gideon_api import gideon_api


def filter_diseases(agent: Optional[int] = None,
                    vector: Optional[str] = None,
                    vehicle: Optional[str] = None,
                    reservoir: Optional[str] = None,
                    country: Optional[str] = None):
    """Filters diseases from the GIDEON API matching the parameters specified.
        Refer to
        https://api-doc.gideononline.com/#4272d285-ba04-435d-b7ad-deabe971330e
        for full specifications
    """

    params = {}

    if agent is not None:
        params['agent'] = agent
    if vector is not None:
        params['vector'] = vector
    if vehicle is not None:
        params['vehicle'] = vehicle
    if reservoir is not None:
        params['reservoir'] = reservoir
    if country is not None:
        params['country'] = country

    # Do not pass an empty dictonary
    if not params:
        params = None

    return gideon_api.query_gideon_api('/diseases/filter', params)
