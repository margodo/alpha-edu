from lion import Lion
from exhibit import Exhibit
from penguin import Penguin

exhibit1 = Exhibit('Happy Zoo','London')

lion = Lion('Rick',age=5)
penguin = Penguin('Carl',age=2)

exhibit1.add_animal(lion)
exhibit1.add_animal(penguin)
exhibit1.show_all_animal()