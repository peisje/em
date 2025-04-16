class Platform:
    def __init__(self, food=100):
        self.food = food

    def add(self, amount):
        self.food += amount

    def remove(self, amount):
        if self.food >= amount:
            self.food -= amount
            return True
        else:
            print("Not enough food!")
            return False

    def info(self):
        return f"Food on the level: {self.food}"


class Level:
    def __init__(self, number):
        self.number = number
        self.platform = Platform(100 if number == 1 else 0)
        self.next = None

    def connect(self, next_level):
        self.next = next_level

    def give(self):
        if self.next and self.platform.food >= 10:
            self.platform.food -= 10
            self.next.platform.food += 10
            print(f"Level {self.number} gave 10 food to level {self.next.number}")
        else:
            print("Not enough food, you died")

    def share(self):
        if self.next and self.platform.food >= 5:
            self.platform.food -= 5
            self.next.platform.food += 5
            print(f"Level {self.number} shared 5 food with level {self.next.number}")
        else:
            print("Not enough food, you died")


class Person:
    def __init__(self, name):
        self.name = name

    def where_am_i(self, level):
        print(f"{self.name} is currently on level {level.number}")


levels = [Level(i + 1) for i in range(10)]
for i in range(9):
    levels[i].connect(levels[i + 1])

current_level_index = 0
current_level = levels[current_level_index]
person = Person("Player")

while True:
    print(f"\nLevel {current_level.number} — actions performed by the person on this level")
    print("1 - Give 10 food to the next level")
    print("2 - Share 5 food with the next level")
    print("3 - Show food")
    print("4 - Go to the next level")
    print("5 - Find out which level I am on")
    print("6 - Exit")

    choice = input("Your choice: ")

    if choice == "1":
        current_level.give()
    elif choice == "2":
        current_level.share()
    elif choice == "3":
        print(current_level.platform.info())
        if current_level.next:
            print("Next level:", current_level.next.platform.info())
    elif choice == "4":
        if current_level_index < len(levels) - 1:
            current_level_index += 1
            current_level = levels[current_level_index]
        else:
            print("You are already at the last level.")
    elif choice == "5":
        person.where_am_i(current_level)
    elif choice == "6":
        print("Game over.")
        break
