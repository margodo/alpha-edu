import pandas as pd

class ExcelCRUD():

    def __init__(self, file_name):
        self.file_name = file_name
    
    def create_excel(self):
        initial_data = {
            'Name': ['Botakoz', 'Forest', 'Dante', 'Jerry'],
            'Age': [18, 30, 22, 26],
            'Grade': ['A', 'C', 'A+', 'D'],
            'Salary': [750, 900, 300, 100],
        }
        original_dataframe = pd.DataFrame(initial_data)
        print(original_dataframe)
        original_dataframe.to_excel(excel_writer=self.file_name, index=False)
        return original_dataframe
    
    def read_excel(self):
        read_excel_dataframe = pd.read_excel(io=self.file_name)
        print(read_excel_dataframe)

    def update_excel(self):
        original_dataframe = pd.read_excel(io=self.name)
        original_dataframe['Experience'] = original_dataframe['Age']-16
        print(original_dataframe)
        original_dataframe['email'] = ['','','','']
        original_dataframe.to_excel(excel_writer=self.file_name, index=False)
        return original_dataframe
    
    def delete_excel(self, df: pd.DataFrame):
        print('Deleting all rows')
        df = df.drop(columns=['email'])
        df = df.drop(index=1) #row = строка
        df.reset_index()
        print('Deleted all rows')
        print(df)




excel_crud_object = ExcelCRUD(file_name='students_data.xlsx')
# excel_crud_object.create_excel()
excel_crud_object.read_excel()