class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_broken = False
    
    def displayInfo(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Is broken:", self.is_broken)

class CarPark:
    def __init__(self, name):
        self.name = name
        
    def breakDown(self):
        self.is_broken = True
        
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
    
    def sendToCenter(self, serviceCenter):
        print(f"{self.name} sent the following cars for repair:")
        for car in self.cars:
            if car.is_broken:
                car.displayInfo()
                serviceCenter.carRepair(car)
                print(f"Car {car.brand} {car.model} has been repaired.")


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


DarjaKovalenko.sendToCenter(bmwCenter)


print(f"Car {car1.brand} {car1.model} status: Broken = {car1.is_broken}")
        
        
