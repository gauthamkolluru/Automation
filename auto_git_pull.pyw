from git_push_all import GitPullPush

pull_status = False

git_pull_obj = GitPullPush()

while pull_status != True:
    pull_status = git_pull_obj.git_pull()
    if pull_status != True:
        print(pull_status)