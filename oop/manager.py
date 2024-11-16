from pprint import saferepr

from employee import Employee

class Manager(Employee):

    def __init__(self,name, salary, bonus):
        super().__init__(name=name, position='manager',salary=salary)
        self.bonus = bonus
        self.calculate_target_cash()

    def calculate_target_cash(self):
        self.salary = self.bonus + self.salary
        return self.salary