from git_push_all import GitPullPush

push_status = False
automation_folder_push_status = False

git_pull_obj = GitPullPush()

while push_status != True:
    push_status = git_pull_obj.git_push()
    if push_status != True:
        print(push_status)

while automation_folder_push_status != True:
    automation_folder_push_status = git_pull_obj.git_push_automation_folder()
    if automation_folder_push_status != True:
        print(automation_folder_push_status)