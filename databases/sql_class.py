import sqlite3  

class DatabaseManager:

    def __init__(self, db_name):
        try:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            print(f"✅ Connection to '{db_name}' was succesful!")
        except sqlite3.Error as error:
            print(f"❌ Error while connecting: {error}")

    def create_table(self, table_name, columns):
        try:
            column_definitions = ""
            for name, dtype in columns.items():
                column_definitions += f"{name} {dtype}, "
            column_definitions = column_definitions.rstrip(", ")
            create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
            self.cursor.execute(create_query)
            self.connection.commit()
            print(f"✅ Table '{table_name}' was created succesfully!")
        except sqlite3.Error as error:
            print(f"❌ Error while creating a table: {error}")

    def insert_data(self, table_name, data):
        try:
            placeholders = ""
            for element in range(len(data[0])):
                placeholders += "?, "  
            placeholders = placeholders.rstrip(", ")
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
            self.cursor.executemany(insert_query, data) 
            self.connection.commit()
            print(f"✅ Data was succesfully inserted to the table '{table_name}'!")
        except sqlite3.Error as error:
            print(f"❌ Error while entering the data: {error}")

    def fetch_all(self, table_name):
        try:
            fetch_query = f"SELECT * FROM {table_name};"
            self.cursor.execute(fetch_query)
            results = self.cursor.fetchall()
            print(f"✅ Received data from the table '{table_name}':")
            for row in results:
                print(row)
            return results
        except sqlite3.Error as error:
            print(f"❌ Error while fetching the data: {error}")
            return []

    def fetch_by_condition(self, table_name, condition):
        try:
            fetch_query = f"SELECT * FROM {table_name} WHERE {condition};"
            self.cursor.execute(fetch_query)
            results = self.cursor.fetchall()
            print(f"✅ Data from table '{table_name}' under the condition '{condition}':")
            for row in results:
                print(row)
            return results
        except sqlite3.Error as error:
            print(f"❌ Error while filtering data: {error}")
            return []

    def update_data(self, table_name, updates, condition):
        try:
            update_query = f"UPDATE {table_name} SET {updates} WHERE {condition};"
            self.cursor.execute(update_query)
            
            self.connection.commit() 

            print(f"✅ Data in the table '{table_name}' was updates sucesfully!")
        except sqlite3.Error as error:
            print(f"❌ Error while updating the data: {error}")

    def delete_data(self, table_name, condition):
        try:
            delete_query = f"DELETE FROM {table_name} WHERE {condition};"
            self.cursor.execute(delete_query)
            self.connection.commit()
            print(f"✅ Data under condition '{condition}' was sucesfully deleted from the table '{table_name}'!")
        except sqlite3.Error as error:
            print(f"❌ Error while deleting data: {error}")


    def change_column_name(self, table_name, old_column_name, new_column_name):

        change_query = f"ALTER TABLE {table_name} RENAME COLUMN {old_column_name} to {new_column_name}"
        self.cursor.execute(change_query)
        self.connection.commit()

        print(f'Column name changed from {old_column_name} to {new_column_name}')

    def close_connection(self):
        self.connection.close()
        print("✅ Connection is closed.")

db = DatabaseManager("students_table.db")

db.create_table(
    table_name="students_table",
    columns={
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT",
        "age": "INTEGER",
        "grade": "REAL",
    }
)

# db.insert_data(
#     table_name="students_table",
#     data=[
#         (None, "Oleg", 22, 100),
#         (None, "Alice", 20, 85.5),
#         (None, "Bob", 22, 90.0),
#         (None, "Charlie", 21, 78.3),
#         (None, "Ken", 19, 75.5),
#         (None, "Barbie", 17, 90.0),
#     ]
# )


db.fetch_all("students_table")

db.fetch_by_condition(table_name="students_table", condition="age > 20")
db.fetch_by_condition(table_name="students_table", condition="age > 20 and grade > 80")
db.fetch_by_condition(table_name="students_table", condition="age > 20 or grade > 91")

db.update_data("students_table", "grade = 89", "name = 'Charlie' and id=4")

# db.change_column_name(table_name="students_table", old_column_name='age', new_column_name='years_from_birth')
# db.change_column_name(table_name="students_table", old_column_name='years_from_birth', new_column_name='age')

# db.delete_data("students_table", "id=5")

db.close_connection()