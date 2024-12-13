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
        print(f'it is a circle with an area of {self.calcArea()}cm^2')
        super().describe()
    
circle1 = Circle(True,'Blue',2.5)

print(circle1.calcArea())
circle1.describe()