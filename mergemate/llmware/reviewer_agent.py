from llmware.prompts import Prompt

class ReviewerAgent:
    def __init__(self):
        self.prompt = Prompt().load_model('gpt-3.5-turbo')
        self.help_commands = {
            '/help': 'List all available commands.',
            '/explain': 'Explain the current code context or a specific part.',
            '/status': 'Get the current status of the PR.'
        }

    def run(self, prompt, context=None):
        header = ":sparkles: **MergeMate Review** :sparkles:\n\n"
        footer = "\n\n:bulb: *Use `/help` to list all available commands.* :bulb:"
        response = self.prompt.prompt_main(
            prompt=prompt,
            context=context
        )
        return header + response + footer
    
    def create_comment(self, comment, event_data):
        if comment.startswith('/'):
            return self.handle_command(comment, event_data)
        else:
            prompt = f"Answer the following: {comment}"
            context = event_data
            return self.run(prompt, context)

    def handle_command(self, command, event_data):
        if command in self.help_commands:
            if command == '/help':
                return '\n'.join([f"{k}: {v}" for k, v in self.help_commands.items()])
            elif command == '/explain':
                return self.explain_code(event_data)
            elif command == '/status':
                return "The PR is currently being reviewed. Changes requested: 2. Comments: 5."
        else:
            return "Command not recognized. Use `/help` to see available commands."

    def create_review(self, pr_details):
        prompt = f"Review the following code changes and provide suggestions: {pr_details['title']} - {pr_details['description']}\n\n"
        return self.run(prompt)

    def explain_code(self, event_data):
        prompt = f"Explain the following code in detail:\n\n{event_data['code_snippet']}"
        return self.run(prompt)
