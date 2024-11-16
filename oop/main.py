from employee import Employee
from manager import Manager
from developer import Developer

accountant = Employee('Peter Grace', 'Accountant', 2000)
developer = Developer('Ivan Schmidt',4000,1000)
manager = Manager('Lora Ten',5000,2000)
intern = Employee('Olga Semenova','Intern',1000)

employees = [accountant,intern,developer,manager]

for employee in employees:
    employee.get_employee_info()