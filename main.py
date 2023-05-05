from github import Github
g = Github("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")

#Get current user---------------------------------------------------------------
user = g.get_user()
user.login
print(user)

#Get user by name----------------------------------------------------------------
user = g.get_user('abcd')
user.name
print(user)

#Get organization by name------------------------------------------------------
org = g.get_organization("NewtGlobal")
org.login
print(org)
#Get repository by name----------------------------------------------------------
repo = g.get_repo("Shajaha-Shaik/newrepo")
repo.name
print(repo)

# #Search repositories by language-------------------------------------------------
# repositories = g.search_repositories(query='language:python')
# for repo in repositories:
#     print(repo)

# #Search repositories based on number of issues with good-first-issue--------------------------
# repositories = g.search_repositories(query='good-first-issues:>3')
# for repo in repositories:
#     print(repo)