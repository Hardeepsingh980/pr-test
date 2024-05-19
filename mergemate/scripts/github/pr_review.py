import os
import json

from mergemate.llmware.reviewer_agent import ReviewerAgent
from mergemate.providers.github import GithubProvider

class PrReviewHandler:
    def __init__(self):
        self.gh = GithubProvider()
        self.agent = ReviewerAgent()
        with open(os.getenv('GITHUB_EVENT_PATH')) as event_file:
            self.event_data = json.load(event_file)
            print("PR event data loaded:", self.event_data)
        
    def run(self):
        pr_details = {
            'title': self.event_data['pull_request']['title'],
            'description': self.event_data['pull_request']['body'],
            # 'code_diff': self.gh.get_pr_diff(self.event_data['pull_request']['number'])
        }
        review_response = self.agent.create_review(pr_details)
        print("Review Response:", review_response)
        self.gh.create_comment(review_response, self.event_data)

if __name__ == "__main__":
    PrReviewHandler().run()
