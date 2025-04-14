import random

class Component:
    def __init__(self, model, manufacturer, power_usage):
        self.model = model
        self.manufacturer = manufacturer
        self.power_usage = power_usage
        
    def get_info(self):
        pass
    
    def run_diagnostic(self):
        pass

    
class CPU(Component):
    def __init__(self, model, manufacturer, power_usage, cores, frequency, temperature, status="OK"):
        super().__init__(model, manufacturer, power_usage)
        self.cores = cores
        self.frequency = frequency
        self.temperature = temperature
        self.status = status
    
    def run_diagnostic(self):
        temp = random.randint(40, 100)
        if temp > 85:
            print("Overheating")
            self.status = "Overheating"
            return False
        self.status = "OK"
        return True


class GPU(Component):
    def __init__(self, model, manufacturer, power_usage, vram, frequency, driver_installed, status="OK"):
        super().__init__(model, manufacturer, power_usage)
        self.vram = vram
        self.frequency = frequency
        self.driver_installed = driver_installed
        self.status = status
        
    def run_diagnostic(self):
        if not self.driver_installed or self.vram < 2:
            self.status = "Missing drivers or low VRAM"
            return False
        self.status = "OK"
        return True


class RAM(Component):
    def __init__(self, model, manufacturer, power_usage, size, frequency, status="OK"):
        super().__init__(model, manufacturer, power_usage)
        self.size = size
        self.frequency = frequency
        self.usage = 0
        self.status = status
    
    def run_diagnostic(self):
        if self.usage > 95 and self.usage < 100 or self.size < 2:
            self.status = "Memory error"
            return False
        self.status = "OK"
        return True
    
    def upgrade(self):
        pass


class Storage(Component):
    def __init__(self, model, manufacturer, power_usage, storage_type, capacity, read_speed, bad_sectors, status="OK"):
        super().__init__(model, manufacturer, power_usage)
        self.storage_type = storage_type
        self.capacity = capacity
        self.read_speed = read_speed
        self.bad_sectors = bad_sectors
        self.status = status
        
    def run_diagnostic(self):
        if self.read_speed < 10 or self.bad_sectors > 100:
            self.status = "Read speed is low or too many bad sectors"
            return False
        self.status = "OK"
        return True
    
    def upgrade(self):
        pass

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

for elem in compArr:
    elem.run_diagnostic()
    print(f"{elem.__class__.__name__} status: {elem.status}")
    
    
    
class Computer:
    def __init__(self):
        self.components = []
        
    def addComponents(self, component):
        self.components.append(component)
        
    def totalPower(self):
        total_power = 0
        for component in self.components:
            total_power += component.power_usage
        return total_power
    
    def diagnosting_all(self):
        for component in self.components:
            if not component.run_diagnostic():
                return f"computer is broken"
            return "it is ok"
        
        
    

computer1 = Computer()

computer1.addComponents(cpu1)
computer1.addComponents(gpu1)
computer1.addComponents(ram1)
computer1.addComponents(storage1)

print(f"Total Power Usage: {computer1.totalPower()}W")

print(f"Computer status: {computer1.diagnosting_all()}")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
