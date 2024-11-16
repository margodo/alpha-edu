class Employee:

    def __init__(self,name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_employee_info(self):
        print(f'Name: {self.name}\nPosition: {self.position}\nSalary: ${self.salary}\n')