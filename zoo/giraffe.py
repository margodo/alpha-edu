from animal import Animal

class Giraffe(Animal):

    def __init__(self, name, age):
        super().__init__(name = name, species='Giraffe', age=age, is_endangered=True)
        self.neck_lenght = 2

    def eat_food(self):
        print(f'{self.species} {self.name} is extending his neck to grab food.')
    
    def dance(self):
        print(f'{self.species} {self.name} is dancing.')