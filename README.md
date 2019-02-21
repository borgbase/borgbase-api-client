# GraphQL Client for BorgBase

A simple GraphQL client to execute operations against your [BorgBase.com](https://www.borgbase.com) account. Can be embedded in all kinds of deployment scripts.

## Setup
Clone this repository

`$ git clone https://github.com/borgbase/borgbase-api-client`

Install requirements

`$ pip install -r requirements.txt`


## Usage
There is an interactive example client in `borgbase_api_client/main.py`. To run the interactive client (will ask for username, password and OTP:
`$ python example.py`

Example session:

```
$ python example.py
Enter Email: test@example.com
Enter Password:
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): api.borgbase.com:443
DEBUG:urllib3.connectionpool:https://api.borgbase.com:443 "POST /graphql HTTP/1.1" 200 38
DEBUG:root:{'data': {'login': {'user': {'id': '3'}}}}
DEBUG:urllib3.connectionpool:https://api.borgbase.com:443 "POST /graphql HTTP/1.1" 200 164
DEBUG:root:{'data': {'sshAdd': {'keyAdded': {'id': '481', 'name': 'Key for VM-004', 'hashMd5': '1e:53:6b:04:86:be:c8:7a:fd:d5:9f:a7:d4:1d:be:9e', 'keyType': 'ssh-ed25519', 'bits': 256}}}}
DEBUG:urllib3.connectionpool:https://api.borgbase.com:443 "POST /graphql HTTP/1.1" 200 141
DEBUG:root:{'data': {'repoAdd': {'repoAdded': {'id': 'y4ab823u', 'name': 'VM-004-test', 'region': 'us', 'repoPath': 'y4ab823u@y4ab823u.repo.borgbase.com:repo'}}}}
INFO:root:Added new repo with path: y4ab823u@y4ab823u.repo.borgbase.com:repo
```

Minimal example as library: 

```python
from borgbase_api_client.client import GraphQLClient
from borgbase_api_client.mutations import *

client = GraphQLClient()
client.login(email='xxx', password='xxx')

new_key_vars = {
    'name': 'Key for VM-004',
    'keyData': 'ssh-ed25519 AAAAC3Nz......aLqRJw+dl/E+2BJ xxx@yyy'
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
print('Added new repo with path:', new_repo_path)
```

## Development
If any features are missing, please open a Github issue against this repo.

Additional functionality can be added by calling different GraphQL queries or mutations in `borgbase_api_client/graphql_queries.py`.

## License (MIT)
Copyright 2019 Manuel Riel for BorgBase

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.