library(reticulate)
use_virtualenv('/home/xh/gideon/python_test/env')
gideon <- import('gideon_api')
gideon$set_api_key(Sys.getenv('GIDEON_API_KEY'))

outbreaks_uk_2013 <- gideon$outbreaks_by_country_year('United Kingdom', 2013)
