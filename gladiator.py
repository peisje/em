
from abc import ABC, abstractmethod
import random

class Person(ABC):
    def __init__ (self, name, power):
        self.name = name
        self.power = power
        
    @abstractmethod
    def talk(self):
        pass
        
        
class Gladiator(Person):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.legion = []
        
    def talk(self):
        print(self.name, "Talk: i am Maksimus, i am collect legion. Power:", self.power)

    def zaverbovat(self, peasant):
        if len(self.legion) < 10:
            if peasant.ready_to_join and peasant.power > 5:
                self.legion.append(peasant)
                print(peasant.name, "zaverbovan v legion")
            else:
                print(peasant.name, "ne zaverbovan v legion")
        else:
            print("legion is full")
            
    def train(self):
        for tsel in self.legion:
            tsel.power += 2
        print("train finish")
            
    def show_legion(self):
        print("legion: ")
        for tsel in self.legion:
            print (tsel.name, "Power:", tsel.power)
    
class Peasant(Person):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.ready_to_join = random.choice([True, False])

    def talk(self):
        print(self.name, "Talk: i am just peasant. Power:", self.power)

krestjan1 = Peasant("Dasa", 6)
krestjan2 = Peasant("lena", 7)
krestjan3 = Peasant("elina", 3)
krestjan4 = Peasant("sonya", 4)
krestjan5 = Peasant("sasa", 8)
krestjan6 = Peasant("igor", 2)

krestjan7 = Peasant("masa", 6)
krestjan8 = Peasant("ksusa", 7)
krestjan9 = Peasant("prikol", 3)
krestjan10 = Peasant("cartman", 4)
krestjan11 = Peasant("kaka", 8)
krestjan12 = Peasant("lol", 2)

villages = [
    {"peasants": [krestjan1, krestjan2], "hz": random.choice([True, False])},
    {"peasants": [krestjan3, krestjan4], "hz": random.choice([True, False])},
    {"peasants": [krestjan5, krestjan6], "hz": random.choice([True, False])}
]

villages2 = [
    {"peasants": [krestjan7, krestjan8], "hz": random.choice([True, False])},
    {"peasants": [krestjan9, krestjan10], "hz": random.choice([True, False])},
    {"peasants": [krestjan11, krestjan12], "hz": random.choice([True, False])}
]

krestjan1.talk()

print(krestjan1.ready_to_join)
maksimus = Gladiator("Maksimus", 100)
maksimus.show_legion()
maksimus.train()


maksimus.zaverbovat(krestjan1)
maksimus.zaverbovat(krestjan2)
maksimus.zaverbovat(krestjan3)
maksimus.zaverbovat(krestjan4)
maksimus.zaverbovat(krestjan5)

maksimus.train()

maksimus.show_legion()
maksimus.talk()


# print(krestjan1.ready_to_join)
# print(krestjan1.power)
# print(krestjan1.name)

# maksimus.power
# maksimus.name

 
 
 
 
 

