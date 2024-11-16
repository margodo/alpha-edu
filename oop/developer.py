from employee import Employee

class Developer(Employee):

    def __init__(self, name, salary, award):
        super().__init__(name=name,position = 'developer',salary=salary)
        self.award = award
        self.calculate_compensation()

    def calculate_compensation(self):
        self.salary = self.award + self.salary
        return self.salary