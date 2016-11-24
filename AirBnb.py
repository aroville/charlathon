from bs4 import BeautifulSoup
import requests
import json
import re

URL_AUTH = 'https://api.airbnb.com/v1/authorize'
URL_SEARCH = 'https://api.airbnb.com/v2/search_results'

USER_NAME = 'nicolas.gallot@gmail.com'  #
CLIENT_ID = '3092nxybyb0otqw18e8nh5nty'  # 138566025676
PASSWORD = 'starter_kit_ds_2017'

ACCESS_TOKEN = 'f07iq32v9gy9t95r38ar30qwk'

# Get access token
data_auth = {
    "client_id": CLIENT_ID,
    "username": USER_NAME,
    "password": PASSWORD
}

# Query API
location = 'France'
# https://api.airbnb.com/v2/search_results?client_id=3092nxybyb0otqw18e8nh5nty&locale=en-US&currency=USD&_format=for_search_results_with_minimal_pricing&_limit=10&_offset=0&fetch_facets=true&guests=1&ib=false&ib_add_photo_flow=true&location=Lake%20Tahoe%2C%20CA%2C%20US&min_bathrooms=0&min_bedrooms=0&min_beds=1&min_num_pic_urls=10&price_max=210&price_min=40&sort=1&user_lat=37.3398634&user_lng=-122.0455164

def get_request_params(offset):
    return {
        'client_id': CLIENT_ID,
        'locale': 'fr-FR',
        'currency': 'EUR',
        '_format': 'for_search_results_with_minimal_pricing',
        'ib_add_photo_flow': 'false',
        'location': location,
        '_limit': 50,
        '_offset': offset
        }

listings = list()
offset = 0
limit = 50

for i in range(0, 2):
    params = get_request_params(offset)
    r = requests.get(URL_SEARCH, params=params)
    print(r.url)
    res = json.loads(r.text)
    listing = res["search_results"]
    listings.append(listing)
    offset += limit
    # listings = listings + listing


print(listing)
