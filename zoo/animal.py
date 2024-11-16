class Animal:

    def __init__(self, name,species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_endangered = False

    def make_sound(sound):
        print(sound)

    def eat_food(food):
        print(f'Feed me with {food}')
    
    def sleep(hrs):
        print(f'I sleep for {hrs} hours')
