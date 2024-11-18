from lion import Lion
from exhibit import Exhibit
from penguin import Penguin
from beaver import Beaver

exhibit1 = Exhibit('happy','London')
exhibit2 = Exhibit('cool', 'London')

lion1 = Lion('Rick',age=5)
lion2 = Lion("Pete", age=4)
penguin = Penguin('Carl',age=2)
beaver = Beaver('Mike', age = 7,weight=16)

exhibit1.add_animal(lion1)
exhibit1.add_animal(penguin)

exhibit2.add_animal(beaver)
exhibit2.add_animal(lion2)

exhibit1.remove_animal(penguin)

exhibit2.show_all_animal()
exhibit1.show_all_animal()