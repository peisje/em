
#1
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         
#     def print_person(self):
#         print(self.name, self.age)
#         
# tom = Person("Tom", 39)
# tom.name = "Jerry"
# tom.print_person()



#2

# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#         
#     def print_person(self):
#         print(self.__name, self.__age)
#      @property   
#     def get_age(self):
#         return self.__age
#     @age.setter
#     def get_age(self, age):
#         if age<0:
#             print("viga: vanus ei sa olla negatiivne")
#             self.__age = age
#     
#         
# tom = Person("Tom", 39)
# tom.__name = "Jerry"
# tom.print_person()
# tom.age = 40
# tom.print-person()
#



#3
# class Student:
#     def __init__(self, name):
#         self.name = name 
#         self.__grades = []
#         
#     def get_grades(self):
#         return self.__grades
#     
#     def add_grade(self, grade):
#         self.__grades.append(grade)
#         
#     def displayInfo(self):
#         print(f"Name: {self.name}, Grades: {self.__grades}")
#         
#     def avgGrade(self):  
#         return sum(self.__grades) / len(self.__grades)
#         
#         
# 
# superStudent = Student("Student")
# superStudent.displayInfo()
# 
# superStudent.add_grade(5)
# superStudent.add_grade(5)
# superStudent.add_grade(2)
# superStudent.displayInfo()
# print(f"Average Grade: {superStudent.avgGrade()}")
# 
# 
# class Course:
#     def __init__(self, title):
#         self.title = title
#         self.__students = []
# 
#     def add_student(self, student):
#         if isinstance(student, Student):
#             self.__students.append(student)  # Corrected this line
#         else:
#             print("Ei saa lisada teisi inimesi")
# 
#     def print_students(self):
#         for student in self.__students:
#             print(student.name)
#             
# superStudent = Student("supeStudent")
# superStudent2 = Student("supeStudent2")
# superStudent3 = Student("supeStudent3")
# 
# 
# superStudent.displayInfo()
# superStudent.add_grade(5)
# superStudent.displayInfo()
# 
# 
# programming = Course("programming")
# programming.add_student(superStudent)
# programming.add_student(superStudent2)
# programming.add_student(superStudent3)
# 
# programming.print_students()


#4

class Animal:
    def __init__(self, paws, eyes, tail):
        self.paws = paws
        self.eyes = eyes
        self.tail = tail

class Mammal(Animal):
    def __init__(self, paws, eyes, tail, name, has_fur):
        super().__init__(paws, eyes, tail)  
        self.name = name
        self.has_fur = has_fur

    def speak(self):
        print(self.name,"- imetaja")

class Dogs(Mammal):
    def __init__(self, paws, eyes, tail, name, has_fur, breed):
        super().__init__(paws, eyes, tail, name, has_fur)  
        self.breed = breed
        
    def speak(self):
        super().speak()
        print("hav hav")


pes = Dogs(4, 2, 1, "Dog", True, "igorek")
print(pes.breed)
pes.speak()
dog = Mammal(4,2,1,"Dog", True)


#5
class Vehicle:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        
    def drive(self, miles):
        self.mileage += miles  # Увеличиваем пробег

class Car(Vehicle):
    def __init__(self, brand, model, mileage, fuel_type):
        super().__init__(brand, model, mileage)  
        self.fuel_type = fuel_type
        
class ElectricCar(Car):  
    def __init__(self, brand, model, mileage, fuel_type, battery_level):
        super().__init__(brand, model, mileage, fuel_type)
        self.battery_level = battery_level
        
    def drive(self, km):
        super().drive(km)  # Передаем km в родительский метод
        self.battery_level -= km  # Уменьшаем уровень заряда

# Создаем объект Vehicle
vehicle = Vehicle("Audi", "RS6", 2000)
print(vehicle.mileage)  # Выведет: 2000

vehicle.drive(1)  
print(vehicle.mileage)  # Выведет: 2001

# Создаем объект ElectricCar
electr = ElectricCar("Tesla", "Cybertruck", 100, "electricity", 100)

electr.drive(2)
print(electr.mileage)  # Выведет: 102 (100 + 2)
print(electr.battery_level)  # Выведет: 98 (100 - 2)
