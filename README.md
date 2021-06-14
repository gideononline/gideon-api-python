# Gideon API Wrapper Roadmap
## Setup
### API KEY
* The package will attempt to read a shell environment variable called `$GIDEON_API_KEY`.
### Future Plans
* `gideon_api_python.set_api_key`
* `gideon_api_python.authorize_user`

## Call the GIDEON API
* `gideon_api_python.query_gideon_api`: This is the main function users should use to send commands to the GIDEON API
* `gideon_api_python.query_gideon_api_online`: This version should be used to process the request without interacting with the cache and provides lower level response data.

## Lookup GIDEON API Identifiers
* `gideon_api_python.lookup_item_id`: User provides a category (diseases, vaccines, etc) and an item to lookup (Cholera, Measles-Mumps-Rubella vaccine, etc) to get the GIDEON specific item code.
Currently this lookup has to match exactly with the item title on the GIDEON dashboard.
### Future plans
* Provide the ability to make close matches, such as omitting the ' vaccine' suffix when searching for a vaccine.

## Query GIDEON database for specific item
* `gideon_api_python.search_gideon_db`: Easy way for users to lookup item when providing a category and id. This should return a JSON.