from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def eat_food(self):
        pass

class Monkey(Animal):
    def eat_food(self):
        print(f"Monkey {self.name} eats meat")

monkey1 = Monkey("dasa")
monkey2 = Monkey("elina")
monkey3 = Monkey("sonya")

animals = [monkey1, monkey2, monkey3]

for animal in animals:
    animal.eat_food()

