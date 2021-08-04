from typing import Optional
from gideon_api import gideon_api


def filter_diseases(agent: Optional[int] = None,
                    vector: Optional[str] = None,
                    vehicle: Optional[str] = None,
                    reservoir: Optional[str] = None,
                    country: Optional[str] = None):
    """Filters diseases matching the specified parameters.

    `API reference for /diseases/filter
    <https://api-doc.gideononline.com/#4272d285-ba04-435d-b7ad-deabe971330e>`_

    Args:
        agent: GIDEON agent code - Classification (e.g., virus, parasite) and
            taxonomic designation.
        vector: GIDEON vector code - An arthropod or other living carrier which
            transports an infectious agent from an infected organism or
            reservoir to a susceptible individual or immediate surroundings.
        vehicle: GIDEON vehicle code - The mode of transmission for an
            infectious agent. This generally implies a passive and inanimate
            (i.e., non-vector) mode.
        reservoir: GIDEON reservoir code - Any animal, arthropod, plant, soil or
            substance in which an infectious agent normally lives and
            multiplies, on which it depends primarily for survival, and where it
            reproduces itself in such a manner that it can be transmitted to a
            susceptible host.
        country: GIDEON country code - In general, this list of country names
            corresponds to accepted geographical and political designations.
            When Country filter is used, it will only retrieve diseases that are
            endemic to the country.

    Returns:
        DataFrame: Returns list of all diseases matching filters. This is a
        valuable tool for the diagnostician. It can be used to create disease
        profiles and to generate reports on the status of diseases in any
        country.
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

    # Do not pass an empty dictionary
    if not params:
        params = None

    return gideon_api.query_gideon_api('/diseases/filter', params)
