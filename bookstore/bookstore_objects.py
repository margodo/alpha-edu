import sqlite3

class Bookstore:
    def __init__(self, name):
        try:
            self.connection = sqlite3.connect(name)
            self.cursor = self.connection.cursor()
            print(f"Connection to '{name}' was succesful!")
        except sqlite3.Error as error:
            print(f"Error while connecting: {error}")

    def create_table(self, table_name, columns):
        try:
            column_definitions = ""
            for name, dtype in columns.items():
                column_definitions += f"{name} {dtype}, "
            column_definitions = column_definitions.rstrip(", ")
            create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
            self.cursor.execute(create_query)
            self.connection.commit()
            print(f"Table '{table_name}' was created succesfully!")
        except sqlite3.Error as error:
            print(f"Error while creating a table: {error}")

    def add_book(self, table_name, data):
        try:
            placeholders = ""
            for element in range(len(data[0])):
                placeholders += "?, "  
            placeholders = placeholders.rstrip(", ")
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
            self.cursor.executemany(insert_query, data) 
            self.connection.commit()
            print(f"Data was succesfully inserted to the table '{table_name}'!")
        except sqlite3.Error as error:
            print(f"Error while entering the data: {error}")

    def delete(self, table_name, condition):
        try:
            delete_query = f"DELETE FROM {table_name} WHERE {condition};"
            self.cursor.execute(delete_query)
            self.connection.commit()
            print(f"Data under condition '{condition}' was sucesfully deleted from the table '{table_name}'!")
        except sqlite3.Error as error:
            print(f"❌ Error while deleting data: {error}")

    def all_books(self, table_name):
        try:
            fetch_query = f"SELECT * FROM {table_name};"
            self.cursor.execute(fetch_query)
            results = self.cursor.fetchall()
            # print(f"✅ Received data from the table '{table_name}':")
            # for row in results:
            #     print(row)
            return results
        except sqlite3.Error as error:
            print(f"❌ Error while fetching the data: {error}")
            return []



    def update_books(self,table_name, updates, condition):
        try:
            update_query = f"UPDATE {table_name} SET {updates} WHERE {condition};"
            self.cursor.execute(update_query)
            
            self.connection.commit() 

            print(f"Data in the table '{table_name}' was updates sucesfully!")
        except sqlite3.Error as error:
            print(f"❌ Error while updating the data: {error}")
    
    def search_book(self, table_name, condition):
        try:
            fetch_query = f"SELECT * FROM {table_name} WHERE {condition};"
            self.cursor.execute(fetch_query)
            results = self.cursor.fetchall()
            for row in results:
                print(row)
            return results
        except sqlite3.Error as error:
            print(f"Error while filtering data: {error}")
            return []
        
    def close_connection(self):
        self.connection.close()
        print("✅ Connection is closed.")

class Buyer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def find_book(self, db_name, name, author, year, genre):
        try:
            fetch_query = f"SELECT * FROM {db_name} WHERE \"name = '{name}' and author = '{author}' and year={year} and genre = '{genre}'\";"
            self.cursor.execute(fetch_query)
            results = self.cursor.fetchall()
            for row in results:
                print(row)
            return results
        except sqlite3.Error as error:
            print(f"Error while filtering data: {error}")
            return []
        
    def buy_book(self, db, db_name, name, author, year, genre):
        found_book = self.find_book(db_name, name, author, year, genre)
        db.update_books(db_name, "amount={found_book}", "name = '{name}'")