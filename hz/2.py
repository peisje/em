#  vozrast ima rabta
class Person:
    def __init__(self,name,age,job):
        self.name= name
        self.age = age
        self.job = job
        print("person created")

    def info(self):
        print(self.name +","+ self.age +","+ self.job)
        
person1 = Person("Dasa", "16", "em")
person2 = Person("Elina", "16", "hz")
person1.info()
person2.info()

