from exhibit import Exhibit
from lion import Lion
from penguin import Penguin
from beaver import Beaver
from giraffe import Giraffe
from zookeeper import Zookeeper
from vet import Vet
from zoo import Zooo

# Creating animals

lion_ricky = Lion('Ricky',6)
lion_peter = Lion('Peter',4)

giraffe_bob = Giraffe('Bob',10)

penguin_lila = Penguin('Lila',13)
penguin_josh = Penguin('Josh',8)
penguin_su = Penguin('Su', 9)

beaver_juan = Beaver('Juan', 6,18)
beaver_inna = Beaver('Inna', 8,20)

# Creating exhibits and adding animal there

exhibit_penguins = Exhibit('Cold Alaska','north')
exhibit_lions = Exhibit('Dangerous Africa','south')
exhibit_giraffes = Exhibit('Tall Africa','east')
exhibit_beavers = Exhibit('Water Dam','west')

exhibit_penguins.add_animal(penguin_josh)
exhibit_penguins.add_animal(penguin_lila)

exhibit_lions.add_animal(lion_peter)
exhibit_lions.add_animal(lion_ricky)

exhibit_beavers.add_animal(beaver_inna)
exhibit_beavers.add_animal(beaver_juan)

exhibit_giraffes.add_animal(giraffe_bob)

#  creating staff

zookeeper_adema = Zookeeper('Adema',25)
zookeeper_mark = Zookeeper('Mark',30)
zookeeper_nurlan = Zookeeper('Nurlan', 22)

vet_gulnaz = Vet('Gulnaz',29)
vet_oleg = Vet('Oleg',37)

# establishing zoo

happy_zoo = Zooo('Happy Zoo', 'Astana')
happy_zoo.add_exhibit(exhibit_beavers)
happy_zoo.add_exhibit(exhibit_giraffes)
happy_zoo.add_exhibit(exhibit_lions)
happy_zoo.add_exhibit(exhibit_penguins)

happy_zoo.add_staff(zookeeper_adema)
happy_zoo.add_staff(zookeeper_mark)
happy_zoo.add_staff(zookeeper_nurlan)
happy_zoo.add_staff(vet_gulnaz)
happy_zoo.add_staff(vet_oleg)

print(f'Hi! Welcome to {happy_zoo.name}. My name is Margarita, let me walk you through it!\n')
happy_zoo.show_info()

# Menu

while True:
    user_input = input('\nHelp me manage my zoo. You can:\n- Type manage_animal to create a new animal,display information about it or see what they can do. After that you need to give me the parameters. \nThe animal will be automatically added to exhibit and zoo.\n\
- Type manage_exhibit to do operation with exhibit. You can create new exhobot, remove animal, add animal or review the info about the exhibit.\n\
- Type manage_zoo to add or remove exhibit. Display daily operations or add new staff.\n\
- Type manage_staff too add new employees or display their operations. New employee will be add to our zoo automatically.\n\
- Type show_info to see current information about the zoo.\n\
- Type q to quit.\n')
    if user_input == 'manage_animal':
        user_operation = input('Choose one of the options (create, see, eat) and type it here:\n')
        if user_operation == 'create':
            new_animal = None
            species = input('Choose: lion, giraffe, beaver, penguin ')
            name = input('Please provide name ')
            age = input('Please provide age ')
            if species == 'beaver':
                weight = input('Please provide weight for the beaver ')
                new_animal = Beaver(name,age,weight)
                exhibit_beavers.add_animal(new_animal)
            elif species == 'lion':
                new_animal = Lion(name,age)
                exhibit_lions.add_animal(new_animal)
            elif species == 'penguin':
                new_animal = Penguin(name,age)
                exhibit_penguins.add_animal(new_animal)
            elif species == 'giraffe':
                new_animal = Giraffe(name,age)
                exhibit_giraffes.add_animal(new_animal)
            else:
                print('invalid answer')
                break
        elif user_operation == 'eat':
            choose_animal = input('Please provide the name of the animal ')
            for exhibit in happy_zoo.list_exhibits:
                for animal in exhibit.animal_list:
                    if choose_animal == animal.name:
                        animal.eat_food()
        elif user_operation == 'see':
            choose_animal = input('Please provide the name of the animal ')
            for exhibit in happy_zoo.list_exhibits:
                for animal in exhibit.animal_list:
                    if choose_animal == animal.name:
                        if animal.species == 'lion':
                            animal.hunt()
                        elif animal.species == 'penguin':
                            animal.swim()
                        elif animal.species == 'beaver':
                            animal.make_dam()
                        elif animal.species == 'giraffe':
                            animal.dance()
    elif user_input == 'manage_exhibit':
        user_operation = input('Choose one of the options (create, remove, add) and type it here:\n')
        if user_operation == 'create':
            new_exhibit = None
            name_exhibit = input('Give this exhibit a name ')
            exhibit_location = input('Provide the location (north,west,east,south) ')
            new_exhibit = Exhibit(name_exhibit,exhibit_location)
            happy_zoo.add_exhibit(new_exhibit)
        elif user_operation == 'add':
            chosen_exhibit = input('Type the name of the exhibit ')
            for exhibit in happy_zoo.list_exhibits:
                if chosen_exhibit == exhibit.name:
                    chosen_animal = input('Please provide the name of the animal ')
                    for exhibit_inner in happy_zoo.list_exhibits:
                        for animal in exhibit_inner.animal_list:
                            if chosen_animal == animal.name:
                                exhibit.add_animal(animal)
                                exhibit_inner.remove_animal(animal)
                                print(f'{animal.name} is removed from {exhibit_inner.name}\n{animal.name} is added from {exhibit.name}')
                                continue
        elif user_operation == 'remove':
            chosen_animal = input('Please provide the name of the animal ')
            for exhibit in happy_zoo.list_exhibits:
                for animal in exhibit.animal_list:
                    if chosen_animal == animal.name:
                        exhibit.remove_animal(animal)
                        print(f'{animal.name} is removed from {exhibit.name}')
    elif user_input == 'manage_staff':
        user_operation = input('Please choose one of the options(add, info)')
        if user_operation == 'add':
            new_employee = None
            name = input('Please provide the name ')
            age = input('Please provide the age ')
            position = input('Please choose the position (vet or zookeeper) ')
            if position == 'vet':
                new_employee = Vet(name,age)
                happy_zoo.add_staff(new_employee)
                print('New vet was welcomed to our zoo!')
            elif position == 'zookeeper':
                new_employee = Zookeeper(name,age)
                happy_zoo.add_staff(new_employee)
                print('New zookeeper was welcomed to our zoo!')
            else:
                print('Invalid input')
        elif user_operation == 'info':
            chosen_employee = input('Please provide the name of employee you want to know more about ')
            for staff in happy_zoo.list_employees:
                if chosen_employee == staff.name:
                    staff.work()
    elif user_input == 'show_info':
        happy_zoo.show_info()
    elif user_input == 'q':
        print('Thank you for helping me!')
        break
    else:
        print('\nWrong input. Please provide valid input.\n')

