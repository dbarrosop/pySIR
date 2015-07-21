import requests
import json

import sir_exceptions

class Call:
    def __init__(self, url, method, params=None):
        if method == 'GET':
            r = requests.get(url, params=params)
        elif method == 'POST':
            r = requests.post(url, json=params)
        elif method == 'PUT':
            r = requests.put(url, json=params)
        elif method == 'DELETE':
            r = requests.delete(url)

        if r.status_code != 200:
            raise sir_exceptions.WrongCallException(r.status_code, r.content)
        elif r.headers['content-type'] != 'application/json':
            raise sir_exceptions.WrongEndpointException('Wrong content-type: {}', format(r.headers['content-type']))

        self.raw_data = r.json()

        if self.raw_data['meta']['error']:
            raise Exception('Something went wrong')

        self.meta = self.raw_data['meta']
        self.parameters = self.raw_data['parameters']
        self.result = self.raw_data['result']
