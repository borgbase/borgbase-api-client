import requests
import logging


class GraphQLClient:
    def __init__(self, token, endpoint="https://api.borgbase.com/graphql"):
        self.endpoint = endpoint
        self.token = token

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def _send(self, query, variables={}):
        data = {"query": query, "variables": variables}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token,
        }

        response = requests.post(self.endpoint, json=data, headers=headers)
        if response.status_code != 200:
            logging.debug(response.text)
            raise Exception(
                "Query failed to run by returning code of {}. {}".format(
                    response.status_code, query
                )
            )

        logging.debug(response.json())
        return response.json()
