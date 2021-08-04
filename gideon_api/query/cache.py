"""Caches the GIDEON API response temporarily to improve response time
    and reduce server utilization
"""
from datetime import datetime as dt
from typing import Any, Dict, Optional
import os.path
import pickle

CACHE_FILE = os.path.join(os.path.dirname(__file__), 'cache.pickle')
TIMESTAMP = 'timestamp'
RESPONSE = 'response'


def is_expired(item_timestamp: dt, now: dt, expiration_hours: int) -> bool:
    """Checks if an item is older than the specified hours"""
    return (now - item_timestamp).total_seconds() >= expiration_hours * 3600


class GideonAPICache:
    """Provides a cache for the API response."""

    def __init__(self,
                 default_expiration_hours: Optional[int] = None,
                 persistent_cache: bool = True,
                 buffer_size: int = 10) -> None:
        """Initializes the API cache settings.

        Args:
            default_expiration_hours: A default duration between the
                time the message was cached and the current moment,
                otherwise the message is considered expired.
            persistent_cache: If true, the cache will be stored between
                sessions on the local file system.
            buffer_size:
                The number of changes to store in memory before writing
                    to the local file system.
        """
        self._cache_dictionary = {}
        self._default_expiration_hours = default_expiration_hours
        self._persistent_cache = persistent_cache
        self._max_buffer = buffer_size
        self._unsaved_changes = 0

        if persistent_cache and os.path.isfile(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                try:
                    self._cache_dictionary = pickle.load(f)
                except PermissionError:
                    pass

    def count_persistent_changes(self, force: bool = False) -> None:
        """Note when the local cache has been updated and periodically
            write changes to the local file system. This method is only
            important when the cache uses the persisten cache option.

        Args:
            force: Force storing the cache, regardless of changes in
                the buffer.
        """
        if self._persistent_cache:
            self._unsaved_changes += 1
            if force or (self._unsaved_changes >= self._max_buffer):
                try:
                    with open(CACHE_FILE, 'wb') as f:
                        pickle.dump(self._cache_dictionary, f)
                    self._unsaved_changes = 0
                except PermissionError:
                    pass

    def delete_old_queries(self,
                           expiration_hours: Optional[int] = None) -> None:
        """Deletes any queries in the local cache that are beyond the
            specified expiration time.

        Args:
            expiration_hours: The time, in hours, from the current
                moment which the cache should be used. If this is not
                specified, the default expiration time will be used.
         """
        # Attempt to set a default expiration time, if exists
        if expiration_hours is None:
            expiration_hours = self._default_expiration_hours

        # Only clear the cache dictionary if a time is set
        now = dt.now()
        if expiration_hours is not None:
            for path in list(self._cache_dictionary.keys()):
                if is_expired(self._cache_dictionary[path][TIMESTAMP], now,
                              expiration_hours):
                    del self._cache_dictionary[path]

    def query(self,
              api_path: str,
              expiration_hours: Optional[int] = None,
              delete_expired_entry: bool = False) -> Optional[Dict[str, Any]]:
        """Attempts to query the local cache file

        Args:
            api_path: The GIDEON API path of the query.
            expiration_hours: The maximum time, in hours, since the
                current moment which a response will be considered
                recent enough.
            delete_expired_entry: Automatically delete the expired
                cached response if it is found, but outside the expired
                hours limit.

        Returns:
            If the path is found, and the most recent update is within
                the expiration_hours, this will return a Python
                dictionary representing the query.
        """
        if api_path in self._cache_dictionary:
            # Try default expiration time if not specified
            if expiration_hours is None:
                expiration_hours = self._default_expiration_hours

            # If there still is not expiration time specified,
            # just return value
            if expiration_hours is None:
                return self._cache_dictionary[api_path][RESPONSE]

            # Only return value if within time limit
            if is_expired(self._cache_dictionary[api_path][TIMESTAMP], dt.now(),
                          expiration_hours):
                if delete_expired_entry:
                    del self._cache_dictionary[api_path]
            else:
                return self._cache_dictionary[api_path][RESPONSE]

    def write(self, api_path: str, value: Dict[str, Any]) -> None:
        """Writes the changes to cache

        Args:
            api_path: The path used to call the query from the API
            value: The JSON, represented as a Python dictionary,
                returned from the server.
        """
        now = dt.now()
        # Check if the query has been stored previously
        if api_path in self._cache_dictionary:
            self._cache_dictionary[api_path][TIMESTAMP] = now
            # Only update and push cache if there is a change
            if value != self._cache_dictionary[api_path][RESPONSE]:
                self._cache_dictionary[api_path][RESPONSE] = value
                self.count_persistent_changes()
        else:
            self._cache_dictionary[api_path] = {
                TIMESTAMP: now,
                RESPONSE: value,
            }
            self.count_persistent_changes()
