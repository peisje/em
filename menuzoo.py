class Food:
    def __init__(self, calories):
        self.calories = calories
        self.food_type = "generic"

class Meat(Food):
    def __init__(self, calories):
        super().__init__(calories)
        self.food_type = "meat"

class Plant(Food):
    def __init__(self, calories):
        super().__init__(calories)
        self.food_type = "plant"

class Fruit(Food):
    def __init__(self, calories):
        super().__init__(calories)
        self.food_type = "fruit"

class Trainable:
    def perform_trick(self):
        pass

class Animal:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def make_sound(self):
        pass

    def eat(self, food):
        pass

    def get_info(self):
        return f"{self.__class__.__name__} - {self.name}, age: {self.age}, weight: {self.weight}"

class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} roars: Roarrr!")

    def eat(self, food):
        if food.food_type == "meat":
            print(f"{self.name} eats meat.")
        else:
            print(f"{self.name} won't eat that.")

class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} trumpets: Tooo!")

    def eat(self, food):
        if food.food_type == "plant":
            print(f"{self.name} eats plants.")
        else:
            print(f"{self.name} won't eat that.")

class Monkey(Animal, Trainable):
    def make_sound(self):
        print(f"{self.name} screams: Ooh-ooh!")

    def eat(self, food):
        print(f"{self.name} eats everything.")

    def perform_trick(self):
        print(f"{self.name} does a backflip!")

class Penguin(Animal, Trainable):
    def make_sound(self):
        print(f"{self.name} says: Quack!")

    def eat(self, food):
        if food.food_type in ["meat", "fruit"]:
            print(f"{self.name} eats the food.")
        else:
            print(f"{self.name} doesn't want to eat that.")

    def perform_trick(self):
        print(f"{self.name} slides on the ice!")

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the zoo.")

    def feed_all(self, food):
        for animal in self.animals:
            animal.eat(food)
        print("All animals have been fed.")

    def make_all_sounds(self):
        for animal in self.animals:
            animal.make_sound()

    def show_all_info(self):
        for animal in self.animals:
            print(animal.get_info())

    def trick_show(self):
        for animal in self.animals:
            if isinstance(animal, Trainable):
                animal.perform_trick()

    def sort_animals(self, by):
        def get_name(animal):
            return animal.name.lower()

        def get_age(animal):
            return animal.age

        def get_weight(animal):
            return animal.weight

        if by == "name":
            self.animals.sort(key=get_name)
        elif by == "age":
            self.animals.sort(key=get_age)
        elif by == "weight":
            self.animals.sort(key=get_weight)

def main():
    zoo = Zoo()
    while True:
        print("\n--- Zoo Menu ---")
        print("1. Add an animal")
        print("2. Feed all")
        print("3. All sounds")
        print("4. Animal info")
        print("5. Tricks")
        print("6. Sort")
        print("7. Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            kind = input("Type (lion, elephant, monkey, penguin): ")
            name = input("Name: ")
            weight = float(input("Weight: "))
            age = int(input("Age: "))

            if kind == "lion":
                zoo.add_animal(Lion(name, weight, age))
            elif kind == "elephant":
                zoo.add_animal(Elephant(name, weight, age))
            elif kind == "monkey":
                zoo.add_animal(Monkey(name, weight, age))
            elif kind == "penguin":
                zoo.add_animal(Penguin(name, weight, age))
            else:
                print("Unsupported animal type.")

        elif choice == "2":
            food_type = input("Food type (meat, plant, fruit): ")
            if food_type == "meat":
                food = Meat(300)
            elif food_type == "plant":
                food = Plant(200)
            elif food_type == "fruit":
                food = Fruit(150)
            else:
                food = None

            if food:
                zoo.feed_all(food)
            else:
                print("Invalid food type.")

        elif choice == "3":
            zoo.make_all_sounds()

        elif choice == "4":
            zoo.show_all_info()

        elif choice == "5":
            zoo.trick_show()

        elif choice == "6":
            sort_by = input("Sort by (name, age, weight): ")
            if sort_by in ["name", "age", "weight"]:
                zoo.sort_animals(sort_by)
                print("Sorting complete. Animals after sorting:")
                zoo.show_all_info()
            else:
                print("Invalid sorting criteria.")

        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()