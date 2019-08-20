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
