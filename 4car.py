class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_broken = False
    
class CarPark:
    def __init__(self, name):
        self.name = name
        
    def breakDown(self):
        self.is_broken = True
        
    def displayInfo(self):
    
class ServiceCenter:
    def __init__(self, name):
        self.name = name
        
    def carRepair(self, car):
        car.is_broken = False
    
class Owner:
    def __init__(self, name):    
        self.name = name
        self.cars = []
        
    def addCars(self, car):
        self.cars.append(car)
    def sendToCenter(self, ServiceCenter):
        print("Kasutaja saatis remondikeskusse sellised autod")
        for car in cars:
            if car.is_broken:
                print()
            serviceCenter
                

bmwCenter = ServiceCenter("BMW center")
car1 = Car("BMW", "E34", 1990)
car1.is_broken = True
        
bmwCenter.carRepair(car1)
print(car1.is_broken)
    
        
        
        
        
