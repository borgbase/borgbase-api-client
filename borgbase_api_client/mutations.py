LOGIN = """
mutation login(
  $email: String!
  $password: String!
  $otp: String
  ) {
    login(
      username: $email
      password: $password
      otp: $otp
    ) {
      user {
        id
      }
    }
}
"""

SSH_ADD = """
mutation sshAdd(
  $name: String!
  $keyData: String!
  ) {
    sshAdd(
      name: $name
      keyData: $keyData
    ) {
      keyAdded {
        id
        name
        hashMd5
        keyType
        bits
      }
    }
}
"""

REPO_ADD = """
mutation repoAdd(
  $name: String
  $quota: Int
  $quotaEnabled: Boolean
  $appendOnlyKeys: [String]
  $fullAccessKeys: [String]
  $alertDays: Int
  $region: String
  $borgVersion: String
  ) {
    repoAdd(
      name: $name
      quota: $quota
      quotaEnabled: $quotaEnabled
      appendOnlyKeys: $appendOnlyKeys
      fullAccessKeys: $fullAccessKeys
      alertDays: $alertDays
      region: $region
      borgVersion: $borgVersion
    ) {
      repoAdded {
        id
        name
        region
        repoPath
      }
    }
}
"""

REPO_EDIT = """
mutation repoEdit(
  $id: String!
  $name: String
  $quota: Int
  $quotaEnabled: Boolean
  $appendOnlyKeys: [String]
  $fullAccessKeys: [String]
  $alertDays: Int
  $borgVersion: String
  $region: String
  ) {
    repoEdit(
      id: $id
      name: $name
      quota: $quota
      quotaEnabled: $quotaEnabled
      appendOnlyKeys: $appendOnlyKeys
      fullAccessKeys: $fullAccessKeys
      alertDays: $alertDays
      borgVersion: $borgVersion
      region: $region
    ) {
      repoEdited {
        id
        name
        region
        repoPath
      }
    }
}
"""
