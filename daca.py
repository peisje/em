Klass 1: Platvorm
class Pl
    def __init__(self):
        self.ressursid = 100

# Klass 2: Tase
class Tase:
    def __init__(self):
        self.ressursid = 0

# Klass 3: Inimene
class Inimene:
    def __init__(self):
        self.ressursid = 0


# Loome objektid
platvorm = Platvorm()
tase = Tase()
inimene = Inimene()

# Platvorm annab ressursse tasemele
print("Platvormil on", platvorm.ressursid, "ressurssi.")
valik1 = input("Kas anda pool tasemele? (jah/ei): ")

if valik1 == "jah":
    antud = platvorm.ressursid // 2
    
