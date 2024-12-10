import sqlite3
from project import Project

class Task_manager:
    def __init__(self, name):
        try:
            self.connection = sqlite3.connect(name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as error:
            print(f"Error while connecting: {error}")

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