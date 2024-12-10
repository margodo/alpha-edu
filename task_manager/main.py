from task import Task
from project import Project

# Task Manager App (With Tkinter or Flask)
# Description: Build a simple to-do list app where users can add, edit, and delete tasks, set deadlines, and track progress.
# OOP Concepts: Create classes for Task, User, and Project. Each class should have methods for updating the task status, deadlines, etc.
# Database: Use SQLite or PostgreSQL to store tasks and user data.
# Tkinter: If you want a desktop app, use Tkinter to create a GUI where users can interact with the task manager.
# Flask: If you prefer a web app, build a Flask app with user login and task management features.

task1 = Task('Wake up', '9:00', 1)
task2 = Task('Stretch', '9:15', 1)
task3 = Task('Breakfast', '9:30', 2)

new_project = Project('Morning routine', '10:00')
new_project.add_task(task1)
new_project.show_info()