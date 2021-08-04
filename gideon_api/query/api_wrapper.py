"""Provides a single point for GIDEON API authorization and queries"""
from datetime import datetime as dt
from time import sleep
from typing import Dict, Optional, Union
from urllib.parse import urlencode
from pandas import DataFrame
import requests
from gideon_api import JSON, PARAMS
from gideon_api.query.cache import GideonAPICache


class Authorization:
    """Maintains the authorization for accessing the GIDEON API"""

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def set_api_key(self, api_key: str) -> None:
        self._api_key = api_key

    def get_authorization_header(self) -> Optional[Dict[str, str]]:
        """Produces a dictionary that can be passed to the requests
            library as a header parameter.
        """
        # Check if key is empty
        if not self._api_key:
            raise ValueError('GIDEON API key not provided')
        return {'Authorization': f'api_key {self._api_key}'}


_API_ORIGIN = 'https://api.gideononline.com'
_BAD_PATH_RESP = {
    'message': "API documentation: 'https://api-doc.gideononline.com'"
}


class GIDEON:
    """Abstraction of querying GIDEON REST API via HTTP"""

    def __init__(self,
                 api_key: Optional[str],
                 delay: Optional[float] = None) -> None:
        self._auth = Authorization(api_key)
        self._cache = GideonAPICache(24, buffer_size=1)
        self._using_delay = delay is not None
        self._delay_period = delay
        self._last_call = None

    def set_api_key(self, api_key: str) -> None:
        self._auth.set_api_key(api_key)

    def query_gideon_api_online(
            self,
            path: str,
            params: Optional[PARAMS] = None,
            return_response_object: bool = False
    ) -> Union[JSON, requests.Response]:
        """Queries the GIDEON API online

        Args:
            path: The path from the GIDEON domain. This string is the
                same as what is listed on the API docs.
            params: A dictionary of key-value pairs which will be
                converted to URL parameters.
            return_response_object: Returns the Response object with
                the entire call instead of just the response.

        Returns:
            A dictionary representing the API response or Response
                object

        Raises:
            ConnectionError: If the request does not return a 200
                status code
        """
        # Pause the execution if a server delay is set
        if self._using_delay and self._last_call is not None:
            time_diff = (dt.now() - self._last_call).total_seconds()
            if time_diff < self._delay_period:
                sleep(time_diff)
        self._last_call = dt.now()

        r = requests.get(_API_ORIGIN + path,
                         params=params,
                         headers=self._auth.get_authorization_header())
        if return_response_object:
            return r
        if r.status_code == 200:
            return r.json()
        if r.status_code == 404:
            raise ValueError(f'Bad GIDEON API path: "{path}" - '
                             'Refer to https://api-doc.gideononline.com')
        raise ConnectionError('Could not connect to GIDEON API')

    def query_gideon_api(
            self,
            api_path: str,
            params: Optional[PARAMS] = None,
            try_dataframe: bool = True,
            force_online: bool = False,
            cache_expiration_hours: Optional[int] = 24
    ) -> Union[DataFrame, JSON]:
        """Queries the GIDEON API either using the local cache or online.

        Args:
            path: The API endpoint to query.
            params: Dictionary key value pairs to be passed.
            try_dataframe: Convert dictionary to pandas DataFrame if possible.
            force_online: Query the API online, rather than the local
                cache. However, the response will still be saved to cache.
            cache_expiration_hours: The number of hours since the present
                moment which a cached response will be considered valid.
                Defaults to 24 hours.

        Returns:
            The API JSON response in the form of a Python dictionary.
        """
        # Create the URL to cache
        uri = api_path
        if isinstance(params, dict):
            uri = f'{uri}?{urlencode(params)}'

        # First try a cached response
        response = self._cache.query(uri, cache_expiration_hours)

        # Try online query if no cache or force online
        if force_online or response is None:
            response = self.query_gideon_api_online(api_path, params)
            if response is not None:
                self._cache.write(uri, response)

        # Check if response should be converted to DataFrame
        if all(
            (try_dataframe, isinstance(response,
                                       dict), len(response.keys()) == 1, 'data'
             in response)):
            try:
                return DataFrame(response['data'])
            except ValueError:
                pass
        return response
