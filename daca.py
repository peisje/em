Klass 1: Platvorm
class Platvorm:
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
    kaod = int(antud * 0.1)
    tegelik = antud - kaod
    platvorm.ressursid -= antud
    tase.ressursid += tegelik
    print("Platvorm andis tasemele", tegelik, "ressurssi.")
else:
    print("Platvorm ei andnud midagi.")

# Tase annab ressursse inimesele
print("\nTasemel on", tase.ressursid, "ressurssi.")
valik2 = input("Kas anda pool inimesele? (jah/ei): ")

if valik2 == "jah":
    antud = tase.ressursid // 2
    kaod = int(antud * 0.1)
    tegelik = antud - kaod
    tase.ressursid -= antud
    inimene.ressursid += tegelik
    print("Tase andis inimesele", tegelik, "ressurssi.")
else:
    print("Tase ei andnud midagi.")

# Tulemused
print("\n--- Lõpptulemused ---")
print("Platvormil:", platvorm.ressursid)
print("Tasemel:", tase.ressursid)
print("Inimesel:", inimene.ressursid)
