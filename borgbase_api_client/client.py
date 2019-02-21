import requests
import logging
from .mutations import *

class GraphQLClient:
    def __init__(self, endpoint='https://api.borgbase.com/graphql'):
        self.endpoint = endpoint
        self.session = requests.session()

    def login(self, **kwargs):
        return self._send(LOGIN, kwargs)

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        request = self.session.post(self.endpoint, json=data, headers=headers)
        if request.status_code != 200:
            logging.debug(request.text)
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
        
        logging.debug(request.json())
        return request.json()
