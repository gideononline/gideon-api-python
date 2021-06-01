"""Provides a single point for authorization and queries"""
from typing import Any, Dict, Optional
import os
import requests

_API_KEY = os.environ['GIDEON_API_KEY']
_API_ORIGIN = 'https://api.gideononline.com'


def api_query(
    path: str, params: Optional[Dict] = None
) -> Optional[Dict[str, Any]]:
    """Queries the GIDEON API

    Args:
        path: The path from the GIDEON domain. This string is the saem as what
            is listed on the API docs.
        params: A dictonary of key-value pairs to add to the URL

    Returns:
        A dictonary representing the API response

    Raises:
        ConnectionError: If the request does not return a 200 status code
    """
    r = requests.get(
        _API_ORIGIN+path,
        params=params,
        headers={'Authorization': f'api_key {_API_KEY}'}
    )
    if r.status_code == 200:
        return r.json()
    raise ConnectionError('Could not connect to GIDEON API')
