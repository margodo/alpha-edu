import sqlite3

class DataBaseManager:

    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        print(f'Connection to database {db_name} is succesful')

    def create_table(self, table_name, columns):
        column_definition = ', '.join([f'{name} {dtype}' for name, dtype in columns.items()])
        create_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({column_definition});'
        try:
            self.cursor.execute
            self.connection.commit()
            print(f'Table {table_name} has been created.')
        except sqlite3.Error as e:
            print('Error while creating the table: {e}')

    # def incertData(self,table_name,data):

if __name__ == '__main__':
    db = DataBaseManager('students.db')
    db.create_table('students',
                    {'id':'INTEGER PRIMARY KEY AUTOINCREMENT',
                    'name': 'TEXT',
                    'age': 'INTEGER',
                    'grade': 'REAL'})
