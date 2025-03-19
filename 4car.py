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
        print("brand: ", brand)
        print("model: ", model)
        print("year: ", year)
        print("seisnud: ")
    
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
        for car in self.cars:
            if car.is_broken:
                car.displayInfo()
            serviceCenter.carRepair(car)
                

bmwCenter = ServiceCenter("BMW center")
car1 = Car("BMW", "E34", 1990)
car1.is_broken = True

car2 = Car("Ferrari", "Ferrari Roma", 2024)
car2.is_broken = True

car3 = Car("VW", "Polo", 1800)

car4 = Car("Toyota", "Corolla", 2020)


DarjaKovalenko = Owner("Darja Kovalenko")
DarjaKovalenko.addCars(car1)
DarjaKovalenko.addCars(car2)
DarjaKovalenko.addCars(car3)
DarjaKovalenko.addCars(car4)

        
bmwCenter.carRepair(car1)
print(car1.is_broken)
        
        
        
        
