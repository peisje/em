class Car:
    def __init__(self,color,engine):
        self.color = color
        self.engine = engine
        print("autode")

    def helloSayer(self):
        print("hello you have" + self.color + " bmw")
        
bmw = Car("Black", "bensiin")
bmw2 = Car("Green", "electr")
print(bmw.color)
print(bmw2.color)
bmw.helloSayer()
