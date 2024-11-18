from animal import Animal

class Beaver(Animal):

    def __init__(self, name, age, weight):
        super().__init__(name=name, age=age, species='Beaver', is_endangered=False)
        self.weight = weight

    def make_sound(self):
        print(f'{self.species} with name {self.name} grumbles')

    def make_dam(self):
        print(f'{self.species} with name {self.name} makes dam')

    def how_heave(self):
        if self.weight < 15:
            print(f'{self.name} is small beaver, it weighs just {self.weight}')
        else:
            print(f'{self.name} is big beaver, it weighs {self.weight}')