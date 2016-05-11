#!/usr/bin/env python
import argparse
import logging
import requests
import sys

# In modules, use `logger = logging.getLogger(__name__)`
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stderr))

def url(host, address):
    return host + '/' + address

class Client(object):
    def __init__(self, remote_base, address):
        self.remote_base = remote_base
        self.address = address

    def _request(self, path):
        return requests.post(url(self.remote_base, path))

    def envs_create(self, env_id):
        resp = self._request('/v1/envs')
        return resp.json()

    def envs_reset(self, env_id):
        self._request('/v1/envs/{}/reset'.format(env_id))

    def envs_step(self, env_id):
        self._request('/v1/envs/{}/step'.format(env_id))

def main():
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('-v', '--verbose', action='count', dest='verbosity', default=0, help='Set verbosity.')
    args = parser.parse_args()

    if args.verbosity == 0:
        logger.setLevel(logging.INFO)
    elif args.verbosity >= 1:
        logger.setLevel(logging.DEBUG)

    client = Client('localhost:3000')
    resp = client.envs_create('CartPole-v0')
    client.envs_reset(resp['id'])
    client.envs_step(resp['id'])

    return 0

if __name__ == '__main__':
    sys.exit(main())
