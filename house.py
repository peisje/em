#nassledovanie,inkasulatsia, i ese 2

class Building:
    def __init__(self,adress, floors, year_built):
        self.__adress = adress
        self.__floors = floors
        self.__year_built = year_built
        self.isRenovate = False
        
    def displayInfo(self):
        print(self.__adress)
        print(self.__floors)
        print(self.__year_built)
        
    def renovate(self, year):
        if self.__year_built > year:
            print("This building cannot be renovated.")
        else:
            self.__year_built = year
            self.isRenovate = True  
            
            
building = Building("laikama 2",5,1900)
building.displayInfo()
building.renovate(2000)
building.displayInfo()


class Library(Building):
    def __init__(self,adress, floors, year_built, books):
        super().__init__(adress, floors, year_built)
        self.books = []
        
    def display_info():
        super().displayInfo()
        print("rammatude arv: ", len(self.books))
      
      
    def listBooks(self):
        for book in self.books:
            print("Nimetus: ", book.tittle,"author: ", book.author,"year: ", book.year)
        
    def borrowBook(self, book):
        if book in self.books:
            self.books.isBorrowed = True 
        else:
            print(f"See rammat on puudub")
    
    def returnBook(self, book):
        self.books.isBorrowed = False
        
    def addBook(self,book):
       self.books.append(book)
       
class Book:
    def __init__(self, title, author, year, date):
        self.tittle = tittle
        self.author = author
        self.year = year
        self.books.isBorrowed = False
        self.date = date
        
        
book = Book("ššikarnoo", "dasa", 1999, "21.03.2014")
library = Library("sõpruse puistee 182", 2, 1867)
library.add_book(book)
        
        

library = Library("Central Library", 3, 1990, 50000)

library.displayInfo()

library.listBooks()









