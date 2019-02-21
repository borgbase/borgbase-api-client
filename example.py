"""
A simple interactive client to add a new VM to your BorgBase account.
"""

import getpass
import logging
logging.basicConfig(level=logging.DEBUG)

from borgbase_api_client.client import GraphQLClient
from borgbase_api_client.mutations import *


email = input('Enter Email: ')
password = getpass.getpass('Enter Password: ')


client = GraphQLClient()
client.login(email=email, password=password)

new_key_vars = {
    'name': 'Key for VM-004',
    'keyData': 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHY/ykTLJA4azIWuu+D6IATFDQY/j5aNj7oW7pxiNk/S manu@nyx2'  # Change!
}
res = client.execute(SSH_ADD, new_key_vars)
new_key_id = res['data']['sshAdd']['keyAdded']['id']

new_repo_vars = {
    'name': 'VM-004-test',
    'quotaEnabled': False,
    'appendOnlyKeys': [new_key_id],
    'region': 'us'
}
res = client.execute(REPO_ADD, new_repo_vars)
new_repo_path = res['data']['repoAdd']['repoAdded']['repoPath']
logging.info('Added new repo with path: %s', new_repo_path)




