from animal import Animal

class Penguin(Animal):
    def __init__(self, name, age):
        super().__init__(name=name, species='penguin', age=age, is_endangered=False)
        self.species = 'penguin'
        
    def swim(self):
        print(f'{self.name} can swim')

    def make_sound(self):
        print(f'{self.name} brays')