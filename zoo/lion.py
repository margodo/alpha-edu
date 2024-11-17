from animal import Animal

class Lion(Animal):

    def __init__(self, name, age):
        super().__init__(name=name, species='lion', age=age, is_endangered=True)
        self.speed = 80

    def make_sound(self):
        print(f'{self.species} {self.name} makes sound roaar.')

    def hunt(self):
        print(f'{self.species} with name {self.name} is hunting.')

    def eat_food(self):
        print(f'{self.name} as {self.species} eats meat.')
