import sqlite3
from project import Project

class TaskManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        # You may want to create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS projects
                               (name TEXT, deadline TEXT)''')
        self.connection.commit()

    def create_table(self, name, columns):
        try:
            column_definitions = ""
            for col_name, dtype in columns.items():
                column_definitions += f"{col_name} {dtype}, "
            column_definitions = column_definitions.rstrip(", ")
            create_query = f"CREATE TABLE IF NOT EXISTS {name} ({column_definitions});"
            self.cursor.execute(create_query)
            self.connection.commit()
            print(f"Table '{name}' was created succesfully!")
        except sqlite3.Error as error:
            print(f"Error while creating a table: {error}")

    def add_project(self, project_name, project_deadline):
        self.cursor.execute("INSERT INTO projects (name, deadline) VALUES (?, ?)",
                            (project_name, project_deadline))
        self.connection.commit()