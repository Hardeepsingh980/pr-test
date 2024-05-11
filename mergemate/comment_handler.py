from github import Github
import os
import json

g = Github(os.getenv('GITHUB_TOKEN'))

with open(os.getenv('GITHUB_EVENT_PATH')) as event_file:
    event_data = json.load(event_file)

repo = g.get_repo(event_data['repository']['full_name'])
issue = repo.get_issue(number=event_data['issue']['number'])    
pr = repo.get_pull(number=event_data['issue']['number'])

comment_body = event_data['comment']['body'].strip().lower()
if "trigger command" in comment_body:
    response = "HELLO WORLD"
    print(f"User Message: {comment_body}\nResponse: {response}")
    issue.create_comment(f"User Message: {comment_body}\nResponse: {response}")
else:
    print("Received non-command comment:", comment_body)

