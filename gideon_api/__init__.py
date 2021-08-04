"""High level access to the GIDEON API wrapper functions

This module automatically handles the necessary authentication with the GIDEON
API. Disease and outbreak information can be called without additional setup.
"""
import os
from typing import Any, Dict, Optional, Union

JSON = Dict[str, Any]
PARAMS = Dict[str, Union[str, int]]

from gideon_api.query import GIDEON

gideon_api = GIDEON(os.environ.get('GIDEON_API_KEY'), 0.5)

from gideon_api.codes import *
from gideon_api.diseases import *


def set_api_key(api_key: str) -> None:
    """Sets the GIDEON API key"""
    gideon_api.set_api_key(api_key)


# Exports query wrapper functions to be visible outside `gideon_api`
def query_online(path: str,
                 params: Optional[PARAMS] = None,
                 return_response_object: bool = False):
    """Queries the GIDEON API and forces a call to the server and ignores local
    caching.

    Args:
        path: The API path as stated in the API documentation.
        params: Optional key-value pairs to attach as URL parameters.
        return_response_object: Indicates if the raw requests object should be
            returned rather than just the data.

    Returns:
        Python dictionary or requests.Response object: Depending on the
        return_response_object variable, either a Python dictionary of the
        returned data or a requests.Response object of the call.
    """
    return gideon_api.query_gideon_api_online(path, params,
                                              return_response_object)


def query(api_path: str,
          params: Optional[PARAMS] = None,
          try_dataframe: bool = True,
          force_online: bool = False,
          cache_expiration_hours: Optional[int] = 24):
    """Query GIDEON API and automatically handles local caching and data type
    conversion.

    Args:
        api_path: The API path as stated in the API documentation.
        params: Optional key-value pairs to attach as URL parameters.
        try_dataframe: If possible, converts output data to pandas dataframe.
        force_online: Forces the query to the server, regardless of cache
            status.
        cache_expiration_hours: Sets the time, in hours, after which a response
            will expire from the cache.

    Returns:
        DataFrame or Python dictionary: The API response will be returned as a
        DataFrame if try_dataframe is True and is applicable to the response
        data or a Python dictionary representing the JSON data.
    """
    return gideon_api.query_gideon_api(api_path, params, try_dataframe,
                                       force_online, cache_expiration_hours)
