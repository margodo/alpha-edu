from animal import Animal

class Exhibit:

    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.animal_list=[]
    
    def add_animal(self,animal:Animal):
        self.animal_list.append(animal)
        return self.animal_list
    
    def remove_animal(self,animal:Animal):
        self.animal_list.remove(animal)

    def show_all_animal(self):
        for animal in self.animal_list:
            print(f'In this exhibit lives {animal.name} - {animal.species}')
        return self.animal_list