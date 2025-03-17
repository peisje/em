class Organization():
    def __init__(self, name,  laptops,employee):
        self.name = name
        self.laptops = laptops 
        self.employee = employee 

    def displaylaptops(self):
        for laptop in self.Laptops:
            print(laptop.model)


class Laptop:
    def __init__(self, brand, ram, storage, year, model):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.year = year
        self.model = model
        
    def updateLaptop(self, ramUpdated=0, storageUpdated=0, yearUpdated=0):
        if ramUpdated != 0:
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
            
    def  giveGift(self,organization,laptop):
        print(organization.name)
        print(laptop.brand)
        organization.laptops.append(laptop)
        
        
Legion = Laptop("lenovo" ,16,512,2012, "XP13")
print(Legion.brand)
Legion.updateLaptop(32)
print(Legion.ram)
print(Legion.year)
print(Legion.storage)
Legion.checkOld()
africa2 = Organization("Africa",[],[])
Legion.giveGift(africa2,legion)