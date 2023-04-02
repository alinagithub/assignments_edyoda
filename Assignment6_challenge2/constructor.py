# Create a class named Dog. It should have a constructor which accepts its name, age and coat color.

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f'Name of the dog is {self.name}\nAge of the dog is {self.age}')

    def get_info(self):
        print(f'Coat color of the dog is {self.coat_color}')


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def get_name(self):
        print("Name of the JackRussellTerrier is", self.name)

    def get_age(self):
        print("Age of the JackRussellTerrier is", self.age)


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def get_name(self):
        print("Name of the Bulldog is", self.name)

    def get_coat(self):
        print("Coat color of the Bulldog is", self.coat_color)


obj1 = Bulldog('Oscar', 1, "Brown")
obj2 = JackRussellTerrier('Simba', 2, "Golden")

obj1.get_name() #prints the name of the Bulldog
obj2.description() #prints the name and age of the JackRussellTerrier
obj1.get_info() #prints the coat color of the Bulldog

# we can add more objects and use functionalities accordingly