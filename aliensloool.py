from rich.console import Console
from rich.table import Table
from rich.text import Text
from time import sleep
import random

console = Console()

class CrewMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.hp = 100
        self.power = random.randint(15, 30)
        self.status = True
        
    def attack_allien():
        pass
    
    def injure():
        pass

class Alien:
    def __init__(self):
        self.aggression = random.randint(1, 10)
        self.hp = 120
        
    def is_alive():
        pass
    def attack():
        pass

class Ship:
    def __init__(self):
        self.rooms = []
        self.status = True
        
        
    def trigger_alarm():
        pass
    def show_status():
        pass
    

class Mission:
    def __init__(self, crewList):
        self.crew = crewList  
        self.alien = Alien()
        self.ship = Ship()
        
    def simulate():
        pass

    def summary(self):
        table = Table(title="Ekipaaz")
        table.add_column("Name", style='yellow')
        table.add_column("Role", style='green')
        table.add_column("Health", style='red')
        table.add_column("Status", style='cyan')

        for crewMember in self.crew:
            status_str = "Alive" if crewMember.status else "Died"
            table.add_row(
                crewMember.name,
                crewMember.role,
                str(crewMember.hp),
                status_str
            )
        console.print(table)

crew = [
    CrewMember("Ripley", "Captain"),  
    CrewMember("Dallas", "Sailor"),
    CrewMember("Ash", "Science Officer"),
    CrewMember("Parker", "Engineer")
]

mission = Mission(crew)
mission.summary()
