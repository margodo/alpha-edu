class Animal:

    def __init__(self, name, species, age, is_endangered:bool):
        self.name = name
        self.species = species
        self.age = age
        self.is_endangered = is_endangered
        # self.__password = 'admin@admin'

    def make_sound(self):
        pass

    def eat_food(self):
        print(f'{self.species}  {self.name} is eating now.')
    
    def sleep(self):
        print(f'{self.species} {self.name} is sleeping now.')

    def get_species(self):
        print(f'{self.name} is {self.species}')

    def display_info(self):
        print(f'{self.name} is {self.species}.\n{self.name} is {self.age} yo.')
        if self.is_endangered == True:
            print(f'{self.species} is endangered')
