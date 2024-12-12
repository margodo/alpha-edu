from task import Task
from project import Project
from tkinter import *
from tkcalendar import Calendar

# Task Manager App (With Tkinter or Flask)
# Description: Build a simple to-do list app where users can add, edit, and delete tasks, set deadlines, and track progress.
# OOP Concepts: Create classes for Task, User, and Project. Each class should have methods for updating the task status, deadlines, etc.
# Database: Use SQLite or PostgreSQL to store tasks and user data.
# Tkinter: If you want a desktop app, use Tkinter to create a GUI where users can interact with the task manager.
# Flask: If you prefer a web app, build a Flask app with user login and task management features.

# -------------- Setting up UI ---------------- 

window = Tk()
window.title("Task Manager")

canvas = Canvas(width=500, height=100,highlightthickness=0)
canvas.create_text(250,50,text='Welcome to task manager',font=('Arial',20,'normal'))
canvas.grid(column=0, row=0, columnspan=2, sticky='EW')

project_name_label = Label(text='Project Name')
project_name_label.grid(column=0, row=1)
project_name = Entry()
project_name.grid(column=1, row=1)
project_deadline_label = Label(text='Project Deadline. Please choose the date')
project_deadline_label.grid(column=0, row=2)
cal = Calendar(window, selectmode = 'day',
               year = 2024, month = 12,
               day = 12)

cal.grid(column=1, row=2)

window.mainloop()
