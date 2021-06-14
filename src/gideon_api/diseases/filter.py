from typing import Optional
from gideon_api import gideon_api, CODE_OR_NAME
from gideon_api.codes import lookup_item


def filter_diseases(agent: Optional[CODE_OR_NAME] = None,
                    vector: Optional[CODE_OR_NAME] = None,
                    vehicle: Optional[CODE_OR_NAME] = None,
                    resivoir: Optional[CODE_OR_NAME] = None,
                    country: Optional[CODE_OR_NAME] = None):
    """Filters diseases from the GIDEON API matching the parameters specified.
        Refer to
        https://api-doc.gideononline.com/#4272d285-ba04-435d-b7ad-deabe971330e
        for full specifications
    """

    if isinstance(agent, str):
        agent = lookup_item('agents', agent)
    if isinstance(vector, str):
        vector = lookup_item('vectors', vector)
    if isinstance(vehicle, str):
        vehicle = lookup_item('vehicles', vehicle)
    if isinstance(resivoir, str):
        resivoir = lookup_item('reservoirs', resivoir)
    if isinstance(country, str):
        country = lookup_item('countries', country)

    params = {}

    if agent is not None:
        params['agent'] = agent
    if vector is not None:
        params['vector'] = vector
    if vehicle is not None:
        params['vehicle'] = vehicle
    if resivoir is not None:
        params['resivoir'] = resivoir
    if country is not None:
        params['country'] = country

    # Do not pass an empty dictonary
    if not params:
        params = None

    return gideon_api.query_gideon_api('/diseases/filter', params)
