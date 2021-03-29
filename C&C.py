
##import pip
from etsy2.oauth import EtsyOAuthClient

##pip.main(['install', 'etsy2'])

from etsy2 import Etsy

etsy = Etsy(api_key="r1dyj98d12hgy6po9e7f6es7")

etsy.findAllFeaturedListings()

etsy_oauth = EtsyOAuthClient(client_key="r1dyj98d12hgy6po9e7f6es7",
                            client_secret="lt4dbjac14",
                            resource_owner_key=oauth_token,
                            resource_owner_secret=oauth_token_secret)
etsy = Etsy(etsy_oauth_client=etsy_oauth)

print (etsy.findAllFeaturedListings())
print (etsy.findAllRegion)

print (etsy.api_url)