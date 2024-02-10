import requests
import json
from config import config


class Rest:
    BASE_URL = config('tcgplayer.url')
    SEARCH_PATH = '/search/request?q={}&isList=false&{}'
    LISTING_PATH = '/product/{}/listings?{}'
    SUFFIX_PARAM = config('tcgplayer.param.key') + '=' + config('tcgplayer.param.value')

    def search(self, query: str, request: json):
        url = (self.BASE_URL + self.SEARCH_PATH).format(query, self.SUFFIX_PARAM)
        res = requests.post(url, json=request)
        return res

    def listing(self, product_id, request: json):
        url = (self.BASE_URL + self.LISTING_PATH).format(product_id, self.SUFFIX_PARAM)
        res = requests.post(url, json=request)
        return res