# Courtney Arrowood & Christy Keinsley March 16, 2021
# Etsy Project
from etsy2.oauth import EtsyOAuthClient
from etsy2 import Etsy

etsy = Etsy(api_key="r1dyj98d12hgy6po9e7f6es7")

listing = etsy.findAllFeaturedListings()

print("THIS IS THE FEATURED INFORMATION: ")
print(len(listing))
print(listing[0])
print(listing[0].keys())

# dict_keys(['listing_id', 'state', 'user_id', 'category_id', 'title', 'description', 
# 'creation_tsz', 'ending_tsz', 'original_creation_tsz', 'last_modified_tsz', 'price',
# 'currency_code', 'quantity', 'sku', 'tags', 'materials', 'shop_section_id', 
# 'featured_rank', 'state_tsz', 'url', 'views', 'num_favorers', 'shipping_template_id',
# 'processing_min', 'processing_max', 'who_made', 'is_supply', 'when_made', 'item_weight',
# 'item_weight_unit', 'item_length', 'item_width', 'item_height', 'item_dimensions_unit',
# 'is_private', 'recipient', 'occasion', 'style', 'non_taxable', 'is_customizable', 'is_digital',
# 'file_data', 'should_auto_renew', 'language', 'has_variations', 'taxonomy_id', 'taxonomy_path',
# 'used_manufacturer', 'is_vintage'])

# print(listing[0]['listing_id'])
# print(listing[0]['category_id'])
# print(listing[0]['title'])
# print(listing[0]['price'])

# Things to explore: findAllFeaturedListings, getInterestingListings, getTrendingListings
# What is the difference between them?

interesting = etsy.getInterestingListings()
trending = etsy.getTrendingListings()

print("THIS IS THE INTERESTING INFORMATION: ")
print(interesting[0])
print(interesting[0].keys())

print("THIS IS THE TRENDING INFORMATION: ")
print(trending[0])

# # Also explore: findAllListingActive
active = etsy.findAllListingActive()

print("THIS IS THE ACTIVE INFORMATION: ")
print(active[0])