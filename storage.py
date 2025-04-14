import random

class Component:
    def __init__ (self,model, manufacturer, power_usage):
        self.model = model
        self.manufacturer = manufacturer
        self.power_usage = power_usage
        
    def get_info(self):
        pass
    
    def run_diagnostic(self):
        pass
        
    
class CPU(Component):
    def __init__ (self, model, manufacturer, power_usage, cores, frequency, temperature, status):
        super().__init__(model, manufacturer, power_usage)
        self.cores = cores
        self.frequency = frequency
        self.temperature = temperature
        self.status = status
    
    def run_diagnostic(self):
        temp = random.randint(40, 100)
        if temp > 85:
            print(overheating)
            return False
        self.status == "OK"
        return True


    
    
    
class GPU(Component):
    def __init__ (self, model, manufacturer, power_usage, vram, frequency, driver_installed, status):
        super().__init__(model, manufacturer, power_usage)
        self.vram = vram
        self.frequency = frequency
        self.driver_installed = driver_installed
        self.status = status
        
    def run_diagnostic(self):
        if not driver_installed or self.vram < 2:
            self.status = "Missing drivers or low VRAM"
            return False
        self.status = status
        return True
        
    
    
class RAM(Component):
    def __init__ (self, model, manufacturer, power_usage, size, frequency):
        super().__init__(model, manufacturer, power_usage)
        self.size = size
        self.frequency = frequency
        self.usage = 0
        
    def run_diagnostic(self):
        if self.usage > 95 and self.usage < 100 or self.size < 2:
            self.status = "memory error"
            return False
        self.status == "OK"
        return True
    
    def upgrade(self):
        pass
        
    
class Storage(Component):
    def __init__ (self, model, manufacturer, power_usage,storage_type, capacity, read_speed, bad_sectors):
        super().__init__(model, manufacturer, power_usage)
        self.storage_type = storage_type
        self.capacity = capacity
        self.read_speed = read_speed
        self.bad_sectors = bad_sectors
        
    def run_diagnostic(self):
        if self.read_speed < 10 or self.bad_sectors > 100:
            self.status = "read speed is low or so many bad_sectors"
            return False
        self.status == "OK"
        return True
        
        
    def storage_type(self):
        pass
    
    def capacity(self):
        pass
        
    def upgrade(self):
        pass
    
    
compArr = []
cpu1 = CPU(
    model="Intel",
    manufacturer="Anton",
    power_usage=60,
    cores=96,
    frequency=2.6,
    temperature=50,
    status="OK")

gpu1 = GPU(
    model="Intel",
    manufacturer="Anton",
    power_usage=320,
    vram=10,
    frequency=1.7,
    driver_installed=True,
    status="OK")

ram1 = RAM(
    model="DDR4",
    manufacturer="Corsair",
    power_usage=15,
    size=16,
    frequency=3200,
    status="OK")

storage1 = Storage(
    model="97 Evo",
    manufacturer="Samsung",
    power_usage=10,
    storage_type="SSD",
    capacity=512,
    read_speed=3500,
    bad_sectors=0,
    status="OK")

compArr = [cpu1, gpu1, ram1, storage1]

compArr.append(cpu1)
compArr.append(gpu1)
compArr.append(ram1)
compArr.append(storage1)

compArr = [cpu1, gpu1, ram1, storage1]

for elem in compArr:
  elem.run_diagnostic()  
    print(f"{elem.__class__.__name__} status: {elem.status}")
    
    
class Computer:
    def __init__ (self, component):
        self.components.append(component)
        
    def totalPower(self):
        pass







        