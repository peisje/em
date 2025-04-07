class Lion:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age
        
    def sound(self):
        print("arrr")
        
class Monkey:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age
        
    def sound(self):
        print("uououo")
        
class Elephant:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age
        
    def sound(self):
        print("uuuu")
        
class Penguin:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age
        
    def sound(self):
        print("krya")
        
        
lion1 = Lion("king", "60", "5")
monkey1 = Monkey("elina", "15", "3")
elephant1 = Elephant("pookie", "100", "7")
penguin1 = Penguin("vasya", "10", "4")

for i in [lion1, monkey1, elephant1, penguin1]:
    i.sound()

