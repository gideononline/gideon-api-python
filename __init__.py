import os
from gideon_api_python.query.api_wrapper import GIDEON

gideon_api = GIDEON(os.environ['GIDEON_API_KEY'], 0.5)
