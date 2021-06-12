from typing import Optional, Union
from gideon_api_python import gideon_api
from gideon_api_python.codes import lookup_item

CODE_OR_NAME = Optional[Union[int, str]]


def filter_diseases(agent: CODE_OR_NAME = None,
                    vector: CODE_OR_NAME = None,
                    vehicle: CODE_OR_NAME = None,
                    resivoir: CODE_OR_NAME = None,
                    country: CODE_OR_NAME = None):

    if isinstance(agent, str):
        agent = lookup_item(gideon_api, 'agents', agent)
    if isinstance(vector, str):
        vector = lookup_item(gideon_api, 'vectors', vector)
    if isinstance(vehicle, str):
        vehicle = lookup_item(gideon_api, 'vehicles', vehicle)
    if isinstance(resivoir, str):
        resivoir = lookup_item(gideon_api, 'reservoirs', resivoir)
    if isinstance(country, str):
        country = lookup_item(gideon_api, 'countries', country)

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
