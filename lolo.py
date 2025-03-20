class Country:
    def __init__(self, name, budget):#8 dolzno bit
        self.name = name
        self.budget = budget
        self.counties = []

    def add_county(self, county):
        self.counties.append(county)

    def approve_funding(self, county, amount, city):
        if self.budget >= amount:
            self.budget -= amount
            county.budget += amount
            city.receive_funding(amount)
            print(f"{self.name} одобрил {amount} финансирования для {city.name} в {county.name}.")
            print(f"{self.name} осталось {self.budget} денег после финансирования.")
        else:
            print(f"{self.name} недостаточно средств для утверждения запроса.")

    def collect_taxes(self):
        total_tax = 0
        for county in self.counties:
            total_tax += county.collect_taxes()
        self.budget += total_tax
        print(f"{self.name} собрал {total_tax} в виде налогов.")
        return total_tax

    def get_budget(self):
        return self.budget


class County:
    def __init__(self, name, budget, cities=None):
        self.name = name
        self.budget = budget
        self.cities = cities if cities else []

    def add_city(self, city):
        self.cities.append(city)

    def process_city_request(self, city, amount):
        if self.budget >= amount:
            self.budget -= amount
            city.receive_funding(amount)
            print(f"{self.name} одобрил {amount} финансирования для {city.name}.")
            print(f"{self.name} осталось {self.budget} денег после финансирования.")
        else:
            print(f"{self.name} недостаточно средств для утверждения запроса.")

    def collect_taxes(self):
        total_tax = 0
        for city in self.cities:
            total_tax += city.collect_taxes()
        self.budget += total_tax
        print(f"{self.name} собрал {total_tax} в виде налогов.")
        return total_tax

    def get_budget(self):
        return self.budget


class City:
    def __init__(self, name, budget, residents=None):
        self.name = name
        self.budget = budget
        self.residents = residents if residents else []

    def request_funding(self, amount, county):
        if county.budget >= amount:
            county.process_city_request(self, amount)
        else:
            print(f"{county.name} недостаточно средств для утверждения запроса для {self.name}.")

    def receive_funding(self, amount):
        self.budget += amount
        print(f"{self.name} получил {amount} финансирования.")
        print(f"{self.name} осталось {self.budget} денег после получения финансирования.")

    def collect_taxes(self):
        total_tax = 0
        for resident in self.residents:
            total_tax += resident.pay_taxes()
        self.budget += total_tax
        print(f"{self.name} собрал {total_tax} в виде налогов.")
        return total_tax

    def add_resident(self, person):
        self.residents.append(person)

    def remove_resident(self, person):
        if person in self.residents:
            self.residents.remove(person)

    def get_info(self):
        return {
            'name': self.name,
            'budget': self.budget,
            'residents': [resident.name for resident in self.residents]
        }


class Person:
    def __init__(self, name, income, city):
        self.name = name
        self.income = income
        self.city = city
        self.city.add_resident(self)

    def pay_taxes(self):
        tax_paid = self.income * 0.1  
        self.city.budget += tax_paid
        print(f"{self.name} заплатил {tax_paid} налогов в {self.city.name}.")
        print(f"{self.city.name} осталось {self.city.budget} денег после уплаты налогов.")
        return tax_paid

    def move_to_city(self, new_city):
        self.city.remove_resident(self)
        self.city = new_city
        new_city.add_resident(self)
        print(f"{self.name} переехал в {new_city.name}.")


country1 = Country("Eesti", 1000000)
country2 = Country("Soome", 800000)


county1 = County("Harju", 500000)
county2 = County("Tartu", 300000)
county3 = County("Pärnu", 200000)


country1.add_county(county1)
country1.add_county(county2)
country2.add_county(county3)


city1 = City("Tallinn", 100000)
city2 = City("Tartu", 50000)
city3 = City("Pärnu", 30000)
city4 = City("Narva", 20000)
city5 = City("Rakvere", 15000)


county1.add_city(city1)
county2.add_city(city2)
county3.add_city(city3)
county3.add_city(city4)
county1.add_city(city5)


person1 = Person("Alice", 50000, city1)
person2 = Person("Bob", 30000, city2)
person3 = Person("Charlie", 25000, city3)
person4 = Person("Elina", 35000, city5)


print("\nЛюди платят налоги:")
person1.pay_taxes()
person2.pay_taxes()
person3.pay_taxes()


print("\nГорода запрашивают деньги у округов:")
city1.request_funding(50000, county1)
city2.request_funding(30000, county2)


print("\nОкруга запрашивают деньги у государства:")
country1.approve_funding(county1, 100000, city1)
country1.approve_funding(county2, 50000, city2)


print("\nЛюди переезжают из одного города в другой:")
person1.move_to_city(city2)
person2.move_to_city(city1)
person4.move_to_city(city5)

print(person1.name)

