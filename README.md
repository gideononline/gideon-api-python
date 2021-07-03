# GIDEON - Python Interface (BETA)

## GIDEON Authentication

- The package will attempt to read the environment variable `$GIDEON_API_KEY`, which is set to your GIDEON API key.
- The GIDEON API key can be updated within Python by calling the function `gideon_api.set_api_key(<YOUR API KEY>)`

## Developer Setup

### Install the Virtual Environment

1. Install the `pipenv` Python package by installing it to your Python user install directory with the following terminal command: `$python3 -m pip install --user pipenv`
2. Setup the developer virtual environment.
   Enter the root of the project and execute the terminal command `$python3 -m pipenv install --dev`
3. Enter the virtual environment with the command `$python3 -m pipenv shell`

### Build and Install the `gideon_api` Package.

- From the root directory, `$pip install -e .`
- The `-e/--editable` flag allows the developer to not have to reinstall the package when the Python files are updated.

### Build the HTML Documentation

1. Navigate to the `docs/` directory
2. Run `make html` to build the HTML documents in the `build/` subdirectory

### Future Plans

- `gideon_api_python.set_api_key`
- `gideon_api_python.authorize_user`

## Quick Tutorial

### GIDEON ID Codes

Many of the items in the GIDEON database use an id code, such as diseases, bacteria, drugs, etc. Use `gideon_api.lookup_item` to get specific item code to use when calling the GIDEON API.

### Outbreak Data

The following command will query the GIDEON API for particular outbreak data:

- `gideon_api.outbreaks_by_year`
- `gideon_api.outbreaks_by_country_year`
- `gideon_api.latest_outbreaks_by_country`
- `gideon_api.outbreaks_by_disease`
- `gideon_api.endemic_countries_by_disease`
- `gideon_api.endemic_diseases_by_country`

## Query the GIDEON API Directly

- `gideon_api.query`: This is the main function users should use to send commands to the GIDEON API
- `gideon_api.query_online`: This version should be used to process the request without interacting with the cache and provides lower level response data.
