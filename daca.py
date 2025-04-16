class Platform:
    def __init__(self, food=100):
        self.food = food

    def add_food(self, amount):
        self.food += amount

    def remove_food(self, amount):
        if self.food >= amount:
            self.food -= amount
        else:
            print("Недостаточно еды!")

    def get_info(self):
        return f"Еда на уровне: {self.food}"


class Level:
    def __init__(self, number):
        self.number = number  # Номер уровня
        self.platform = Platform()  # Платформа создаётся автоматически
        self.next_level = None  # Связь с другим уровнем (если будет)

    def connect_next(self, next_level):
        self.next_level = next_level  # Связываем уровень с другим

    def make_decision(self):
        print(f"\nВы на уровне {self.number}. Еды: {self.platform.food}")
        print("Меню:")
        print("1 - Оставить еду себе")
        print("2 - Передать еду на следующий уровень")
        print("3 - Поделиться едой с другим уровнем")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            print("Еду оставили себе.")
        elif choice == "2":
            self.give_food()
        elif choice == "3":
            self.share_food()
        else:
            print("Некорректный выбор!")

    def give_food(self):
        if self.next_level:
            amount = 20
            self.platform.remove_food(amount)
            self.next_level.platform.add_food(amount)
            print(f"Уровень {self.number} передал {amount} еды уровню {self.next_level.number}.")
        else:
            print("Следующего уровня нет.")

    def share_food(self):
        if self.next_level:
            amount = 10
            self.platform.remove_food(amount)
            self.next_level.platform.add_food(amount)
            print(f"Уровень {self.number} поделился {amount} еды с уровнем {self.next_level.number}.")
        else:
            print("Следующего уровня нет.")

# Создаём платформы
platform1 = Platform(100)
platform2 = Platform(50)

# Создаём уровни и связываем их
level2 = Level(platform2)
level1 = Level(platform1, next_level=level2)

# Создаём людей
alice = Person("Алиса")
bob = Person("Боб")

# Алиса принимает решение на первом уровне
alice.act(level1)
print(platform1.get_info())
print(platform2.get_info())

# Боб принимает решение на втором уровне
bob.act(level2)

#
print(platform2.get_info())
lvl1 = Level(1)
lvl2 = Level(2)

# Связываем уровни
lvl1.connect_next(lvl2)

# Пример действий
lvl1.make_decision()
print(lvl1.platform.get_info())
print(lvl2.platform.get_info())




