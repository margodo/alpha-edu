class Task:
    def __init__(self, description: str, deadline: str, priority: int):
        self.description = description
        self.deadline = deadline
        self.priority = priority

    def task_description(self):
        return f'{self.description}. Deadline: {self.deadline}. Has priority: {self.priority}.'
