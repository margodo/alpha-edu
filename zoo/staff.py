class Staff():

    def __init__(self,name,position,age):
        self.name = name
        self.position = position
        self.age = age

    def work(self):
        print(f'{self.name} works as {self.position}.')

    def report_exhibit(self,exhibit):
        print(f'{self.name} as {self.position} is reporting:\n{exhibit.exhibit_info()}.')

    def report_animal(self,animal):
        print(f'{self.name} as {self.position} is reporting:\n{animal.display_info()}.')

