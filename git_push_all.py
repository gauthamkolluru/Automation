import os
import sys
import subprocess


class GitPullPush:
    def __init__(self):
        self.nothing_to_commit = b"On branch master\nYour branch is up to date with 'origin/master'.\n\nnothing to commit, working tree clean\n"
        # self.root_dir = os.path.join(os.path.expanduser('~'), 'Documents/CodingLabs')
        self.root_dir = os.path.join(os.path.expanduser('~'), 'Documents')
        self.dir_list = [directory for directory in os.listdir(self.root_dir) if os.path.exists(
            os.path.join(os.path.join(self.root_dir, directory), '.git'))]

    def git_pull(self):
        try:
            print('Automation')
            subprocess.run(['git', 'pull'], cwd=os.path.join(
                os.path.expanduser('~'), 'Automation'), shell=True)
            for directory in self.dir_list:
                print(directory)
                subprocess.run(['git', 'pull'], cwd=os.path.join(
                    self.root_dir, directory), shell=True)
        except Exception as er:
            return repr(er)
        return True

    def git_push(self):
        try:
            for directory in self.dir_list:
                print(directory)
                subprocess.run(['git', 'pull'], cwd=os.path.join(
                    self.root_dir, directory), shell=True)
                subprocess.run(['git', 'add', '.'], cwd=os.path.join(
                    self.root_dir, directory), shell=True)
                git_status = subprocess.run(['git', 'status'], cwd=os.path.join(
                    self.root_dir, directory), shell=True, capture_output=True)
                if self.nothing_to_commit not in git_status.stdout:
                    print(git_status.stdout)
                    self.commit_message = input("Enter Commit Message: ")
                    subprocess.run(['git', 'commit', '-m', self.commit_message], cwd=os.path.join(
                        self.root_dir, directory), shell=True)
                    subprocess.run(['git', 'push'], cwd=os.path.join(
                        self.root_dir, directory), shell=True, capture_output=True)
        except Exception as er:
            return repr(er)
        return True

    def git_push_automation_folder(self):
        try:
            print('Automation')
            subprocess.run(['git', 'pull'], cwd=os.path.join(
                os.path.expanduser('~'), 'Automation'), shell=True)
            subprocess.run(['git', 'add', '.'], cwd=os.path.join(
                os.path.expanduser('~'), 'Automation'), shell=True)
            git_status = subprocess.run(['git', 'status'], cwd=os.path.join(
                os.path.expanduser('~'), 'Automation'), shell=True, capture_output=True)
            if self.nothing_to_commit not in git_status.stdout:
                print(git_status.stdout)
                self.commit_message = input("Enter Commit Message: ")
                subprocess.run(['git', 'commit', '-m', self.commit_message], cwd=os.path.join(
                    os.path.expanduser('~'), 'Automation'), shell=True)
                subprocess.run(['git', 'push'], cwd=os.path.join(
                    os.path.expanduser('~'), 'Automation'), shell=True, capture_output=True)
        except Exception as er:
            return repr(er)
        return True


if __name__ == "__main__":
    git_obj = GitPullPush()
    pull_status = git_obj.git_pull()
    if pull_status != True:
        print(pull_status)
    push_status = git_obj.git_push()
    if push_status != True:
        print(push_status)
    automation_folder_push_status = git_obj.git_push_automation_folder()
    if automation_folder_push_status != True:
        print(automation_folder_push_status)
