from task import Task
from project import Project
from tkinter import *
from tkcalendar import Calendar
from task_manager import TaskManager

# Task Manager App (With Tkinter)
# Description: Build a simple to-do list app where users can add, edit, and delete tasks, set deadlines, and track progress.
# OOP Concepts: Create classes for Task and Project. Each class should have methods for updating the task status, deadlines, etc.
# Database: Use SQLite or PostgreSQL to store tasks and user data.
# Tkinter: If you want a desktop app, use Tkinter to create a GUI where users can interact with the task manager.
# Flask: If you prefer a web app, build a Flask app with user login and task management features.

# ----------- get date functionality ------------------- 
def date():
    selected_date = cal.get_date()  # Get the selected date from the calendar
    project_deadline.set(selected_date)  # Update the project deadline entry with selected date

# ----------- create project functionality ------------- 
def create_project():
    project_name_value = input_user.get()  # Get the project name entered by the user
    project_deadline_value = project_deadline.get()  # Get the selected deadline
    
    if project_name_value and project_deadline_value:  # Make sure both are provided
        projects_db.add_project(project_name_value, project_deadline_value)
        print(f"Project '{project_name_value}' created with deadline {project_deadline_value}")

# ----------------------- UI Setup ----------------------
window = Tk()
window.title("Task Manager")
window.config(padx=20, pady=20)

input_user = StringVar(window)
project_deadline = StringVar(window)

canvas = Canvas(width=500, height=100, highlightthickness=0)
canvas.create_text(250, 50, text='Welcome to Task Manager', font=('Arial', 20, 'normal'))
canvas.grid(column=0, row=0, columnspan=2, sticky='EW')

project_name_label = Label(text='Project Name', pady=20)
project_name_label.grid(column=0, row=1)
project_name = Entry(textvariable=input_user)
project_name.grid(column=1, row=1)

project_deadline_label = Label(text='Project Deadline. Please choose the date')
project_deadline_label.grid(column=0, row=2)

deadline_label = Label(textvariable=project_deadline, pady=20)
deadline_label.grid(column=1, row=2)

select_button = Button(text='Select Date', command=date)
select_button.grid(row=3, column=0)

create_button = Button(text='Create', command=create_project)
create_button.grid(row=4, column=0, columnspan=2, sticky='EW', pady=15)

cal = Calendar(window, selectmode='day', year=2024, month=12, day=12)
cal.grid(column=1, row=2, rowspan=2, sticky='EW')

# ----------------------- creating DB ----------------------
projects_db = TaskManager('my_projects.db')

window.mainloop()