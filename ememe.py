from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat_food(self):
        pass

class Monkey(Animal):
    def eat_food(self):
        print("Monkey eats meat")
    
    def __repr__(self):
        return "Monkey()"


monkey1 = Monkey()
monkey2 = Monkey()
monkey3 = Monkey()


animals = [monkey1, monkey2, monkey3]



monkey1.eat_food()  
