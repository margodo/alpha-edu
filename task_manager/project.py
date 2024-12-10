from task import Task

class Project:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.tasks = []

    def add_task(self, task: Task):
        self.tasls = self.tasks.append(task)
        print('appended')
        return self.tasks
    
    def show_info(self):
        print(f'{self.name} project has following tasks:\n')
        print(self.tasks[0].task_description())
        
    