REPO_DETAILS = '''
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
'''