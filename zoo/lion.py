from animal import Animal

class Lion(Animal):

    def __init__(self, name, species, age):
        super().__init__(name, species, age)
        self.name = name
        self.species = 'lion'
        self.age = age

    def make_sound(self):
        return super().make_sound('Roar')