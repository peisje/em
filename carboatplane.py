class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("drive")
        
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("sail")
        
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("fly")
        
car1 = Car("ford", "mustang")
boat1 = Boat("ibiza", "touring 20")
plane1 = Plane("Boeing", "747")

for i in [car1,boat1,plane1]:
    i.move()