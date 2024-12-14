from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop (self):
        pass
    
class Car(Vehicle):
    def go(self):
        print('You start the vehicle')
    def stop(self):
        print('You stopped the vehicle')
        
car1 = Car()

car1.go()

class Shape:
    def __init__(self,is_filled,color):
        self.is_filled = is_filled
        self.color = color
    def describe(self):
        print(f'it is {self.color} and {'filled' if self.is_filled else 'not filled'}')
        
class Circle(Shape):
    def __init__(self, is_filled, color,radius):
        super().__init__(is_filled, color)
        self.radius = radius
    def calcArea (self):
        return 3.142*self.radius**2
    def describe(self):
        print(f'it is a circle with an area of {self.calcArea()}cm')
        super().describe()
    
circle1 = Circle(True,'Blue',2.5)
 
print(circle1.calcArea())
circle1.describe()

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
    def add_books(self,book):
        self.books.append(book)
    def list_books(self):
        return [f'{book.name}' for book in self.books]
        
class Book:
    def __init__(self,name):
        self.name = name
 
 
book1 = Book('Harry Potter xvx')       
book2 = Book('Fantastic Mr. Fox')       
book3 = Book('Shaolin Monks')       
book4 = Book('The intellingent Monger')  

library1 = Library('Northern X insight ')  

library1.add_books(book1)   
library1.add_books(book2)   
library1.add_books(book3)   
library1.add_books(book4)

print(library1.list_books() )  