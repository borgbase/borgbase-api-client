

import os
from borgbase_api_client.client import GraphQLClient

TOKEN = os.environ.get("TOKEN")
client = GraphQLClient(TOKEN)


def repo_exists(name):
    """
    Given a repository name, see if a repository with this name already exists.

    :param name: the name to search for
    :returns: returns True if repo with name exists, False otherwise
    """
    query = """ 
    {
      repoList {
        id
        name
      }
    }
    """

    res = client.execute(query)
    for repo in res['data']['repoList']:
        if repo['name'] == name:
            return True

    return False

if __name__ == '__main__':
    print("Repo with name exists:", repo_exists('web18'))