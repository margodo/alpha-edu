from staff import Staff

class Vet(Staff):

    def __init__(self, name, age):
        super().__init__(name=name, position='Vet', age=age)

    def check_health(self,animal):
        print(f'{self.position} is checking health of {animal.species} {animal.name}')