REPO_DETAILS = """
query repoList {
  repoList {
    id
    name
    quota
    quotaEnabled
    lastModified
    currentUsage
  }
}
"""

FILTER_REPOS_BY_NAME = """
{
  repoList(name: "web20") {
    id
    name
    quota
    quotaEnabled
    lastModified
    currentUsage
  }
}
"""

SINGLE_REPO_BY_ID = """
query {
  repo(repoId: "xxx999") {
    id
    name
    quota
    quotaEnabled
    lastModified
    currentUsage
  }
}
"""

KEY_DETAILS = """
query repoList {
  sshList {
    id
    name
    keyData
    keyType
    bits
    comment
    hashMd5
    addedAt
  }
}
"""
