
class Platform:
    def __init__(self, food=0):
        self.food = food

    def show_food(self):
        print("Food on this platform:", self.food)
def kill_next_level(self, next_platform):
        if next_platform:
            next_platform.food = 0
            print("Next level has been destroyed! 💀 All food is gone.")
        else:
            print("No next level to destroy.")
class Level:
    def __init__(self, number, food):
        self.number = number
        self.food = food
        self.next = None
        self.people = []

    def give_food(self):
        if self.next and self.food >= 10:
            self.food -= 10
            self.next.food += 10
            print("Gave 10 food to next level")
        else:
            print("Not enough food you are died")

    def share_food(self):
        if self.next and self.food >= 5:
            self.food -= 5
            self.next.food += 5
            print("Shared 5 food with next level")
        else:
            print("Not enough food to share, you are died")

    def show_food(self):
        print("Food on this level:", self.food)
        if self.next:
            print("Food on next level:", self.next.food)





class Person:
    def __init__(self, name):
        self.name = name

    def who_is_here(self, level):
        # Show who is on the current level
        if level.people:
            print(f"People on level {level.number}:")
            for person in level.people:
                print(f"- {person.name}")
        


# === Create people ===
person1 = Person("pers1")
person2 = Person("pers2")
person3 = Person("pers3")
person4 = Person("pers4")
person5 = Person("pers5")
person6 = Person("pers6")
person7 = Person("pers7")
person8 = Person("pers8")
person9 = Person("pers9")
person10 = Person("pers10")

# === Create levels ===
level1 = Level(1, 100)
level2 = Level(2, 0)
level3 = Level(3, 0)
level4 = Level(4, 0)
level5 = Level(5, 0)
level6 = Level(6, 0)
level7 = Level(7, 0)
level8 = Level(8, 0)
level9 = Level(9, 0)
level10 = Level(10, 0)

# === Connect levels ===
level1.next = level2
level2.next = level3
level3.next = level4
level4.next = level5
level5.next = level6
level6.next = level7
level7.next = level8
level8.next = level9
level9.next = level10

# === Assign people to levels ===
level1.people.append(person1)
level2.people.append(person2)
level3.people.append(person3)
level4.people.append(person4)
level5.people.append(person5)
level6.people.append(person6)
level7.people.append(person7)
level8.people.append(person8)
level9.people.append(person9)
level10.people.append(person10)

# === Player ===
player = Person("Player")
current_level = level1

# === Menu ===
while True:
    print("\nYou are on level", current_level.number)
    print("1 - Give 10 food to next level")
    print("2 - Share 5 food with next level")
    print("3 - Show food")
    print("4 - Go to next level")
    print("5 - Who i am?")
    print("6 - Exit")
    print("7 - Destroy next level (remove all its food)")

    choice = input("Your choice: ")

    if choice == "1":
        current_level.give_food()
    elif choice == "2":
        current_level.share_food()
    elif choice == "3":
        current_level.show_food()
    elif choice == "4":
        if current_level.next:
            current_level = current_level.next
        else:
            print("You are already at the last level.")
    elif choice == "5":
        player.who_is_here(current_level)  # Now calls the `who_is_here()` method of Person
    elif choice == "6":
        print("Game over.")
    elif choice == "7":
     if current_level.next:
        current_level.platform.kill_next_level(current_level.next.platform)
    else:
        print("No next level to destroy.")

        
