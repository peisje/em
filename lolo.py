#self eto element mkotori pomogaet obrasatsa  vnutrenim dannim klassa
class Country:
    def __init__(self, name, population, budget, currency, area, capital, language):
        self.name = name
        self.population = population
        self.budget = budget
        self.currency = currency
        self.area = area
        self.capital = capital
        self.language = language
        self.counties = []        
        
    def add_county(self, county):
        self.counties.append(county)
        
    def approve_funding(self, county, summa, city):
        if self.budget >= summa:
            self.budget -= summa
            county.budget += summa
            print(f"Approved funding of {summa} for {city.name} in {county.name}.")
        else:
            print("Not enough funds in the country.")
        
    def collect_taxes(self):
        total_taxes = sum(county.collect_taxes() for county in self.counties)
        self.budget += total_taxes
        print(f"Country collected taxes. New budget: {self.budget}")
        
    def get_budget(self):
        return self.budget


class County:
    def __init__(self, name, population, budget, area):
        self.name = name
        self.population = population
        self.budget = budget
        self.area = area
        self.cities = []
        
    def add_city(self, city):
        self.cities.append(city)
        
    def process_city_request(self, city, summa):
        if self.budget >= summa:
            self.budget -= summa
            city.receive_funding(summa)
            print(f"City {city.name} received {summa} from county {self.name}.")
        else:
            print(f"Not enough funds in the county {self.name} for {city.name}.")
    
    def request_government_support(self, summa, city):
        print(f"County {self.name} requests {summa} from the country for city {city.name}.")
        return summa
    
    def collect_taxes(self):
        total_taxes = sum(city.collect_taxes() for city in self.cities)
        self.budget += total_taxes
        return total_taxes
    
    def get_budget(self):
        return self.budget


class City:
    def __init__(self, name, population, budget):
        self.name = name
        self.population = population
        self.budget = budget
        self.citizens = []
        
    def request_funding(self, summa):
        print(f"City {self.name} is requesting {summa} from the county.")
        return summa
    
    def receive_funding(self, summa):
        self.budget += summa
    
    def collect_taxes(self):
        taxes = self.population * 100  
        self.budget += taxes
        print(f"City {self.name} collected taxes. New budget: {self.budget}")
        return taxes
    
    def add_resident(self, person):
        self.citizens.append(person)
        self.population += 1
        print(f"Resident {person.name} added to {self.name}. Population: {self.population}")
    
    def remove_resident(self, person):
        self.citizens.remove(person)
        self.population -= 1
        print(f"Resident {person.name} removed from {self.name}. Population: {self.population}")
    
    def get_info(self):
        return f"City {self.name}, Population: {self.population}, Budget: {self.budget}"


class Person:
    def __init__(self, name, age, currency, city):
        self.name = name
        self.age = age
        self.currency = currency
        self.city = city
        city.add_resident(self)  
        
    def pay_taxes(self):
        tax_amount = 100  
        self.city.budget += tax_amount
        print(f"{self.name} paid taxes in {self.city.name}.")
    
    def move_to_city(self, new_city):
        self.city.remove_resident(self)
        self.city = new_city
        new_city.add_resident(self)
        print(f"{self.name} moved to {new_city.name}.")
        
        

country1 = Country("Estonia", 500000, 1000000, "euro", 55000, "Tallinn", "estonian")
country2 = Country("Germany", 19000000, 1500000, "euru", 330000, "Gamburg", "germanian")


county1 = County("Harjumaa", 50000, 600000, 97699)
county2 = County("Võrumaa", 50000, 50000, 96999)
county3 = County("Tartumaa", 476, 38000, 80000) 

country1.add_county(county1)
country1.add_county(county2)
country2.add_county(county3)


city1 = City("Tartu", 60000, 500000)
city2 = City("Tallinn", 80000, 300000)
city3 = City("Aya napa", 120000, 700000)
city4 = City("Afins", 60000, 200000)
city5 = City("Funsal", 150000, 900000)


county1.add_city(city1)
county1.add_city(city2)
county2.add_city(city3)
county3.add_city(city4)
county3.add_city(city5)


person1 = Person("Dasa", 20, 50000, city1)
person2 = Person("Lena", 25, 40000, city2)
person3 = Person("Elina", 20, 60000, city3)
person4 = Person("Boris", 30, 7000, city3)


person1.pay_taxes()
person2.pay_taxes()


city1.request_funding(200000)
county1.process_city_request(city1, 200000)


county1.request_government_support(500000, city1)
country1.approve_funding(county1, 500000, city1)


person1.move_to_city(city3)

person4.move_to_city(city1)
