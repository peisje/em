class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
   
person1 = Employee("dasa", "10", "pro")
person2 = Employee("lena", "9", "medium")
person3 = Employee("elina", "11", "noob")

    def giveGift(self, organization, laptop):
            print(organization.name)
            print(laptop.brand)
            organization.laptops.append(laptop)  






class Organization:
    def __init__(self, name, laptops, employees):
        self.name = name
        self.laptops = laptops
        self.employees = employees

    def displayLaptops(self):
        for laptop in self.laptops:
            print(laptop.model)def giveGift(self, organization, laptop):
        print(organization.name)
        print(laptop.brand)
        organization.laptops.append(laptop)  


class Laptop:
    def __init__(self, brand, ram, storage, year, model):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.year = year
        self.model = model
        
    def updateLaptop(self, ramUpdated=0, storageUpdated=0, yearUpdated=0):
        if ramUpdated != 0:def giveGift(self, organization, laptop):
        print(organization.name)
        print(laptop.brand)
        organization.laptops.append(laptop)  
            self.ram = ramUpdated 
        if storageUpdated != 0:
            self.storage = storageUpdated
        if yearUpdated != 0:
            self.year = yearUpdated
             
    def checkOld(self):
        if self.year < 2020:
            print("old")
        else:
            print("not old")
            
    def giveGift(self, organization, laptop):
        print(organization.name)
        print(laptop.brand)
        organization.laptops.append(laptop)  


legion = Laptop("Lenovo", 16, 512, 2012, "XP13")
print(legion.brand)
legion.updateLaptop(32)
print(legion.ram)
print(legion.year)
print(legion.storage)
legion.checkOld()
africa2 = Organization("Africa", [], [])

legion.giveGift(africa2, legion)

africa2.displayLaptops()
