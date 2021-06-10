"""Provides a single point for authorization and queries"""
from datetime import datetime as dt
from time import sleep
from typing import Any, Dict, Optional, Union
from urllib.parse import urlencode
import requests
from gideon_api_python.query.cache import GideonAPICache


class Authorization:
    """Maintains the authorization for accessing the GIDEON API"""
    def __init__(self, api_key: Optional[str] = None) -> None:
        self._api_key = api_key
        self._using_key = api_key is not None

    def get_authorization_header(self):
        """Produces a dictonary that can be passed to the requests
            library as a header parameter.
        """
        auth = f'api_key {self._api_key}' if self._using_key else None
        return {'Authorization': auth}


_API_ORIGIN = 'https://api.gideononline.com'
_BAD_PATH_RESP = {
    'message': "API documentation: 'https://api-doc.gideononline.com'"
}


class GIDEON:
    def __init__(self,
                 api_key: Optional[str],
                 delay: Optional[float] = None) -> None:
        self._auth = Authorization(api_key)
        self._cache = GideonAPICache(24, buffer_size=1)
        self._using_delay = delay is not None
        self._delay_period = delay
        self._last_call = None


    def query_gideon_api_online(
        self,
        path: str,
        params: Optional[Dict] = None,
        return_response_object: bool = False
    ) -> Union[Optional[Dict[str, Any]], requests.Response]:
        """Queries the GIDEON API online

        Args:
            path: The path from the GIDEON domain. This string is the
                same as what is listed on the API docs.
            params: A dictonary of key-value pairs which will be
                converted to URL parameters.
            return_response_object: Returns the Response object with
                the entire call instead of just the response.

        Returns:
            A dictonary representing the API response or Response
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

        r = requests.get(
            _API_ORIGIN+path,
            params=params,
            headers=self._auth.get_authorization_header()
        )
        if return_response_object:
            return r
        if r.status_code == 200:
            return r.json()
        if r.status_code == 404:
            raise ValueError(
                f'Bad GIDEON API path: "{path}" - '
                'Refer to https://api-doc.gideononline.com'
            )
        raise ConnectionError('Could not connect to GIDEON API')


    def query_gideon_api(
        self,
        api_path: str,
        params: Optional[Dict] = None,
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
        # Create the URL to cache
        uri = api_path
        if isinstance(params, dict):
            uri = f'{uri}?{urlencode(params)}'

        # First try a cached response
        cached_respone = self._cache.query(uri, cache_expiration_hours)
        if force_online or cached_respone is None:
            online_respone = self.query_gideon_api_online(api_path, params)
            if online_respone is not None:
                self._cache.write(uri, online_respone)
                return online_respone
        return cached_respone
