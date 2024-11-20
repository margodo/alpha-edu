class Zooo:

    def __init__(self,name, city):
        self.name = name
        self.list_exhibits = []
        self.list_employees = []
        self.city = city

    def add_exhibit(self,exhibit):
        self.list_exhibits.append(exhibit)

    def add_staff(self,employee):
        self.list_employees.append(employee)

    def daily_operation(self):
        for employee in self.list_employees:
            for exhibit in self.list_exhibits:
                for animal in exhibit.animal_list:
                    if employee.position == 'Vet':
                        employee.check_health(animal)
                    elif employee.position == 'Zookeper':
                        employee.feed(animal)

    def show_info(self):
        for exhibit in self.list_exhibits:
            exhibit.exhibit_info()
            exhibit.show_all_animal()
            print('')
        for employee in self.list_employees:
            employee.work()
