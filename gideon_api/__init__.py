import os
from typing import Any, Dict, Optional, Union

JSON = Dict[str, Any]
PARAMS = Dict[str, Union[str, int]]
CODE_OR_NAME = Union[int, str]

from gideon_api.query import GIDEON

gideon_api = GIDEON(os.environ['GIDEON_API_KEY'], 0.5)

from gideon_api.codes import *
from gideon_api.diseases import *


# Exports query wrapper functions to be visible outside `gideon_api`
def query_online(path: str,
                 params: Optional[PARAMS] = None,
                 return_response_object: bool = False):
    return gideon_api.query_gideon_api_online(path, params,
                                              return_response_object)


def query(api_path: str,
          params: Optional[PARAMS] = None,
          try_dataframe: bool = True,
          force_online: bool = False,
          cache_expiration_hours: Optional[int] = 24):
    return gideon_api.query_gideon_api(api_path, params, try_dataframe,
                                       force_online, cache_expiration_hours)
