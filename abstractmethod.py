# class Animal:
#     def make_sound():
#         pass
#     
# class Dog(Animal):
#     pass
# 
# dog1 = Dog()
# dog1.make_sound()
# 
# from abc import ABC, abstractmethod
# 
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#     
# class Dog(Animal):
#     pass
# 
# 
# dog2 = Dog()
# dog2.make_sound()

# zadanie
from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self):
        self.state = {
            "health": 100,
            "inventory": [],
            "morale": 1.0
        }
    
    @abstractmethod
    def decide_action(self):
        pass
    
    @abstractmethod
    def update_state(self):
        pass

# 1. Civilian class
class Civilian(Character):
    def decide_action(self, context):
#         print(context[1])
        if context[1]["danger_level"]> 0.6:
            print("Civilian is hiden")
        else:
            print("Civilian tryied fight")
    
    def update_state(self):
        if context[1]["danger_level"]> 0.6:
            self.state["morale"] -= 0.3
        else:
            self.state["morale"] += 0.5

# 2. Criminal class
class Criminal(Character):
    def decide_action(self, context):
        if context[1]["danger_level"]> 0.8  and context["Civilian"]["danger_level"]< 0.9 :
            print("steal")
        elif context[1]["danger_level"]> 0.5 and context["Civilian"]["danger_level"]< 0.8 :
            print("fight")
        else:
            print("run")
    
    def update_state(self):
        if context[1]["danger_level"]> 0.9:
            self.state["morale"] -= 0.5
        else:
            self.state["morale"] += 0.1

# 3. Survivor class
class Survivor(Character):  
    def decide_action(self):
        if context[1]["danger_level"]> 0.8  and context["Civilian"]["danger_level"]< 0.9 :
            print("steal")
        elif context[1]["danger_level"]> 0.5 and context["Civilian"]["danger_level"]< 0.8 :
            print("fight")
        else:
            print("run")
    
    def update_state(self):
        if context[1]["danger_level"]> 0.9:
            self.state["morale"] -= 0.5
        else:
            self.state["morale"] += 0.10


civilian1 = Civilian()
criminal1 = Criminal()
survivor1 = Survivor()
people = [civilian1,criminal1,survivor1]

print(civilian1.state["health"])

context = {
    "Civilian": {
        "danger_level": 0.3,
        "has_weapon": False,
        "health": 60
    },
    "Criminal": {
        "danger_level": 0.6,
        "has_weapon": True,
        "health": 90
    },
    "Survivor": {  
        "danger_level": 0.4,
        "has_weapon": False,
        "health": 70
    }
}


print(context["Civilian"]["danger_level"])

# 1
# for elem in context:
#     print(elem)
# 2

myRandom = random.choice(list(context.items()))
print(myRandom)

for elem in people:
    elem.decide_action(myRandom)
    


for elem in context:
    print(context[elem]["danger_level"])



















