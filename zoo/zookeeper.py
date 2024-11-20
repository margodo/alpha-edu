from staff import Staff
import random

duties = ['is doing great job.', 'is not really diligent.','forgets to clean the exhibits.', 'is senior professional in taking care of animal.']

class Zookeeper(Staff):

    def __init__(self, name, age):
        super().__init__(name=name, age=age, position='Zookeper')
        self.duty = random.choice(duties)

    def feed(self,animal):
        print(f'{self.position} {self.name} is feeding {animal.species} {animal.name}')