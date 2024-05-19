from github import Github
import os


class GithubProvider:
    def __init__(self):
        self.g = Github(os.getenv('GITHUB_TOKEN'))

    def get_repo(self, full_name):
        return self.g.get_repo(full_name)

    def get_issue(self, repo, number):
        return repo.get_issue(number=number)

    def get_pull(self, repo, number):
        return repo.get_pull(number=number)

    def create_comment(self, body, event_data):
        repo = self.get_repo(event_data['repository']['full_name'])
        issue = self.get_issue(repo, number=event_data['issue']['number'])
        issue.create_comment(body)

    def get_comment_body(self, event_data):
        return event_data['comment']['body'].strip().lower()
        

    

    