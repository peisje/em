class Platform:
    def __init__(self, food=100):
        self.food = food  # Уровень начинается с 100 еды

    def add_food(self, amount):
        self.food += amount  # Добавляем еду

    def remove_food(self, amount):
        if self.food >= amount:
            self.food -= amount  # Убираем еду
        else:
            print("Недостаточно еды!")

    def get_info(self):
        return f"Еда на уровне: {self.food}"


class Level:
    def __init__(self, platform):
        self.platform = platform  # Привязываем платформу с едой к уровню

    def make_decision(self):
        action = input("Что сделать? (оставить/передать/поделиться): ").strip().lower()

        if action == "оставить":
            print("Еду оставили себе.")
        elif action == "передать":
            self.give_food_to_next_level()
        elif action == "поделиться":
            self.share_food()
        else:
            print("Некорректное действие!")

    def give_food_to_next_level(self):
        loss = self.platform.food * 0.2  # Потеря 20% при передаче
        transferred_food = self.platform.food - loss
        print(f"Передали еду на следующий уровень. Потеряно {loss} еды.")
        self.platform.remove_food(self.platform.food)

    def share_food(self):
        shared_food = self.platform.food / 2
        self.platform.remove_food(shared_food)
        print(f"Поделились едой. Осталось {self.platform.food} еды.")


# Создаём платформу с едой
lvl1 = Platform(100)
lvl2 = Platform(80)

# Создаём уровни
level1 = Level(lvl1)
level2 = Level(lvl2)

# Пример принятия решения на первом уровне
level1.make_decision()
print(lvl1.get_info())

# Пример принятия решения на втором уровне
level2.make_decision()
print(lvl2.get_info())
