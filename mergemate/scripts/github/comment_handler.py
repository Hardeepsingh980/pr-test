import os
import json

from mergemate.llmware.reviewer_agent import ReviewerAgent
from mergemate.providers.github import GithubProvider



class CommandHandler:
    def __init__(self):
        self.gh = GithubProvider()
        self.agent = ReviewerAgent()
        with open(os.getenv('GITHUB_EVENT_PATH')) as event_file:
            self.event_data = json.load(event_file)
            print(self.event_data)
        
    def run(self):
        comment_body = self.gh.get_comment_body(self.event_data)
        response = self.agent.create_comment(comment_body, self.event_data)
        print(response)
        self.gh.create_comment(response, self.event_data)


if __name__ == "__main__":
    CommandHandler().run()