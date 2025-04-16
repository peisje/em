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
            print("Недостаточно еды!")
            return False

    def info(self):
        return f"Еда на уровне: {self.food}"


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
            print(f"Уровень {self.number} передал 10 еды уровню {self.next.number}")
        else:
            print("Недостаточно еды ты умер")

    def share(self):
        if self.next and self.platform.food >= 5:
            self.platform.food -= 5
            self.next.platform.food += 5
            print(f"Уровень {self.number} поделился 5 еды с уровнем {self.next.number}")
        else:
            print("Недостаточно еды ты умер")


class Person:
    def __init__(self, name):
        self.name = name

    def where_am_i(self, level):
        print(f"{self.name} сейчас на уровне {level.number}")


levels = [Level(i + 1) for i in range(10)]
for i in range(9):
    levels[i].connect(levels[i + 1])

current_level_index = 0
current_level = levels[current_level_index]
person = Person("Игрок")

while True:
    print(f"\nуровень {current_level.number} — действия выполняет человек на этом уровне")
    print("1 - Передать 10 еды")
    print("2 - Поделиться 5 едой")
    print("3 - Показать еду")
    print("4 - Перейти на следующий уровень")
    print("5 - Узнать, на каком я уровне")
    print("6 - выйти")

    choice = input("Ваш выбор: ")

    if choice == "1":
        current_level.give()
    elif choice == "2":
        current_level.share()
    elif choice == "3":
        print(current_level.platform.info())
        if current_level.next:
            print("Следующий уровень:", current_level.next.platform.info())
    elif choice == "4":
        if current_level_index < len(levels) - 1:
            current_level_index += 1
            current_level = levels[current_level_index]
        else:
            print("Вы уже на последнем уровне.")
    elif choice == "5":
        person.where_am_i(current_level)
    elif choice == "6":
        print("Игра завершена.")
        break

    
        