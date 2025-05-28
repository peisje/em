from rich.console import Console
from rich.table import Table
import random
from time import sleep

console = Console()

class CrewMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.hp = 100
        self.power = random.randint(15, 30)
        self.status = True
        
    def attack_alien(self, alien):
        if self.status:
            damage = self.power + random.randint(-5, 5)
            alien.hp -= damage
            if alien.hp < 0:
                alien.hp = 0
            console.print(f"[bold green]{self.name} attacked alien for {damage} damage. Alien HP left: {alien.hp}")
    
    def injure(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.status = False
            self.hp = 0
            console.print(f"[red]{self.name} {self.role} was killed by alien[/red]")
        else:
            console.print(f"[yellow]{self.name} {self.role} took {damage} damage! HP left: {self.hp}[/yellow]")
        

class Alien:
    def __init__(self):
        self.aggression = random.randint(1, 10)
        self.hp = 120
        
    def is_alive(self):
        return self.hp > 0
        
    def attack(self, crew):
        alive_crew = [member for member in crew if member.status]
        if alive_crew:
            target = random.choice(alive_crew)
            damage = random.randint(15, 40) + self.aggression
            console.print(f"[magenta]Alien attacks {target.name} for {damage} damage![/magenta]")
            target.injure(damage)
        else:
            console.print("[magenta]No crew left to attack.[/magenta]")

class Ship:
    def __init__(self):
        self.rooms = ["engine room", "Medical block", "warehouse", "rest room", "navigation center"]
        self.status = "All systems are running by default"
        
    def trigger_alarm(self, room):
        console.print(f"[bold red]ALARM! Alien presence detected in location: {room}[/bold red]")
        console.print(f"[bold red]{self.status}[/bold red]")
        
    def show_status(self):
        console.print(f"[blue]Ship status: {self.status}[/blue]")


class Mission:
    def __init__(self, crewList):
        self.crew = crewList  
        self.alien = Alien()
        self.ship = Ship()
        
    def simulate(self):
        console.print(f"[bold green]The mission begins[/bold green]")
        self.ship.show_status()
        sleep(1)
        
        for round in range(1, 11):
            if not self.alien.is_alive():
                console.print(f"[bold green]The crew defeated the alien![/bold green]")
                break
            console.print(f"[bold]Round {round}[/bold]")
            room = random.choice(self.ship.rooms)
            console.print(f"[cyan]Scanning room: {room}[/cyan]")
            sleep(1)
            if random.random() < 0.7 and self.alien.is_alive():
                self.ship.trigger_alarm(room)
            
            alive_crew = []
            for member in self.crew:
                if member.status and self.alien.is_alive():
                    member.attack_alien(self.alien)
            
            if self.alien.is_alive():
                self.alien.attack(self.crew)
            
            sleep(1)

        console.print("\n[bold underline]Mission summary:[/bold underline]")
        self.summary()

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
mission.simulate()

