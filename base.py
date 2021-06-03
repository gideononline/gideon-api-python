"""Provides a single point for authorization and queries"""
from typing import Any, Dict, Optional, Union
import os
import requests
from gideon_api_python.cache import GideonAPICache

_API_KEY = os.environ['GIDEON_API_KEY']
_API_ORIGIN = 'https://api.gideononline.com'
_BAD_PATH_RESP = {
    'message': "API documentation: 'https://api-doc.gideononline.com'"
}

cache = GideonAPICache(24)


def online_query(
    path: str,
    return_response_object: bool = False
) -> Union[Optional[Dict[str, Any]], requests.Response]:
    """Queries the GIDEON API online

    Args:
        path: The path from the GIDEON domain. This string is the saem as what
            is listed on the API docs.
        return_response_object: Returns the Response object with the entire call
            instead of just the response.

    Returns:
        A dictonary representing the API response or Response object

    Raises:
        ConnectionError: If the request does not return a 200 status code
    """
    r = requests.get(
        _API_ORIGIN+path,
        headers={'Authorization': f'api_key {_API_KEY}'}
    )
    if return_response_object:
        return r
    if r.status_code == 200:
        query_response = r.json()
        if query_response != _BAD_PATH_RESP:
            return r.json()
        raise ValueError((
            f'Bad GIDEON API path: "{path}" - '
            'Refer to https://api-doc.gideononline.com'
        ))
    raise ConnectionError('Could not connect to GIDEON API')


def api_query(
    api_path: str,
    force_online: bool = False,
    cache_expiration_hours: Optional[int] = 24
) -> Optional[Dict[str, Any]]:
    """Queries the GIDEON API either using the local cache or online.

    Args:
        path: The API endpoint to query.
        force_online: Query the API online, rather than the local
            cache. However, the respoonse will still be saved to cache.
        cache_expiration_hours: The number of hours since the present
            moment which a cached response will be considered valid.
            Defaults to 24 hours.

    Returns:
        The API JSON response in the form of a Python dictonary.
    """
    cached_respone = cache.query(api_path, cache_expiration_hours)
    if force_online or cached_respone is None:
        online_respone = online_query(api_path)
        if online_respone is not None:
            cache.write(api_path, online_respone)
            return online_respone
    return cached_respone
