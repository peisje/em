class Platform:
    def __init__ (self, food=100):
        self.food = []
        
        
    def addfood(self, amount):
        self.food += amount
        
    def removefood(self):
        if self.food >= amount:
            self.food -= amount
        else:
            print("not enough food")
    
    def getinfo(self):
        return f"food on level: {self.food}"
    
    
    
class Level:
    def __init__ (self, number):
        self.number = number
        self.platform = Platform ()
        self.nextlevel = none
        
    def connect_next(self, next_level):
        self.next_level = next_level
  
  
    def giveanotherlvl(self):
        if self.next_level:
            amount = 20
            self.platform.remove_food(amount)
            self.next_level.platform.add_food(amount)
            print(f"Level {self.number} share {amount} food with level {self.next_level.number}.")
        else:
            print("naxt level dont exist.")
            
    def share_food(self):
        if self.next_level:
            amount = 10
            self.platform.remove_food(amount)
            self.next_level.platform.add_food(amount)
            print(f"level {self.number} shre {amount} food with level {self.next_level.number}.") 
        else:
            print("next level doesny exist")
            
    def takeall(self):
        print("ypu take all food", self.food, "all died")
    
class People:
    def __init__(self, name):
        self.name = name
        
    def actionlvl(self, level):
        print(f"{self.name} act on level {level.number}:")
    
people = [People(f"Person{i}") for i in range(1, 11)]

# levels = [Level(i) for i in range(1, 11)]
# 
# 
# for i in range(len(levels) - 1):
#     levels[i].connect_next(levels[i + 1])
# 
# current_level = levels[0]  
    



pers1 = People("person1")
pers2 = People("person2")
pers3 = People("person3")
pers4 = People("person4")
pers5 = People("person5")
pers6 = People("person6")
pers7 = People("person7")
pers8 = People("person8")
pers9 = People("person9")
pers10 = People("person10")




 
      

    
    
#    
platform1 = Platform(50)
platform2 = Platform(10)

lvl1 = Platform(1)
lvl2 = Platform(2)
lvl3 = Platform(3)
lvl4 = Platform(4)
lvl5 = Platform(5)
lvl6 = Platform(6)
lvl7 = Platform(7)
lvl8 = Platform(8)
lvl9 = Platform(9)
lvl10 = Platform(10)
# print(lvl1.addfood)
# print(lvl2.removefood)
# print(lvl3.getinfo)

# pers1.act(lvl1)
print(platform1.getinfo())
print(platform2.getinfo())

# lvl1.connect_next(lvl2)


# lvl1.make_decision()
# print(lvl1.platform.get_info())
# print(lvl2.platform.get_info())






while True:
    print("menu:")
    print("1 - take food yourself")
    print("2 - give food another lvl")
    print("3 - share food with someone")
    print("4 - share food with platform")
    print("5 - kill all")
    print("6 - bye")
 
    choice = input("your choise: ").strip()
 
    if choice == "1":
        print("you take your food.")

    elif choice == "2":
        current_level.give_another_lvl()

    elif choice == "3":
        current_level.share_food()


    elif choice == "4":
        print(current_level.platform.get_info())
        if current_level.next_level:
            print(current_level.next_level.platform.get_info())
        else:
            print("No next level.")
            
    elif choice == "5":
        lvl1.takeall()
       
    elif choice =="6":
       print("bye")
       break
    else:
        print("choise dont correct!")
            
