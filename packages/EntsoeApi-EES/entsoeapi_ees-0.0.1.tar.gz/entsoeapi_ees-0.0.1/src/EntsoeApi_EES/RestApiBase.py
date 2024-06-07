import requests
import json
import urllib.parse
import logging
import os

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))

class RestApiBase:

    def __init__(self, base_url):
        self.base_url = base_url

    def _process_query_params(self, params):
        query_param_string = ''
        sep = '?'
        for key, value in params.items():
            key_url_encoded = urllib.parse.quote_plus(key)
            value_url_encoded = urllib.parse.quote_plus(value)
            query_param_string += f'{sep}{key_url_encoded}={value_url_encoded}'
            sep = '&'
        return query_param_string

    def _do_http_call(self, url, http_headers={}):
        try:
            return self._process_response(requests.get(url, headers=http_headers))
        except Exception:
            logger.info(f'Request exception occurred on url {url} method')

    def _process_response(self, response):
        if response.status_code in range(200,207):
            return response.content
        elif response.status_code == 404:
            logger.info(f"api url not found {response.request.url}")
        else:
            logger.info(f"api request failed HTTP statuscode: {response.status_code} Url: {response.request.url}")
            logger.info(response.content)
        return None

    def get_request(self, url : str, query_params : dict ={} , http_headers: dict ={}):
        '''
        Does a get request to the specified URL and returns parsed json as a result. 
        :param str url: the url string where the GET request is send to excluding the Base URL
        :param dict query_params: dictionary of queryparameters that need to be appended to the URL
        :param dict http_headers: dictionary of additional http headers that the GET request should contain
        '''
        request_url = f'{self.base_url}{url}{self._process_query_params(query_params)}'
        return self._do_http_call(request_url, http_headers=http_headers)