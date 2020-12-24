"""
A simple interactive client to add a new ssh-key to existing repository.
"""
import os
import logging

logging.basicConfig(level=logging.DEBUG)

from borgbase_api_client.client import GraphQLClient
from borgbase_api_client.mutations import *
from borgbase_api_client.queries import *

# Create new client by passing the API token
TOKEN = os.environ.get("TOKEN")
client = GraphQLClient(TOKEN)

# Send test request
client.execute("{ isAuthenticated }")

# Add new SSH key
new_key_vars = {
    'name': 'Key added through GraphQL API',
    'keyData': 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMmdI2GFNWgZN3jyIlbed+gRQOT0x2zTaTCe/BKPqpsw jobroe@machine'
}
res = client.execute(SSH_ADD, new_key_vars)
new_key_id = res['data']['sshAdd']['keyAdded']['id']

# Add new SSH key to existing repo
# Note: The id and at least one further variable is required.
#       To figure out the repo id query repoList, check repo-exist example.
repo_vars = {
    "id": "px0yc6u8",
    "appendOnlyKeys": [new_key_id]
}
res = client.execute(REPO_EDIT, repo_vars)
repo_path = res["data"]["repoEdit"]["repoEdited"]["repoPath"]
logging.info("Edited repo with path: %s", repo_path)
