from car import Car 

car1 = Car('Toyota','Tundra','blue','Boruto')

car1.drive()
car1.drive()
car1.drive()
car1.drive()
print(car1.accelerate)


class Student: 
    class_year = 2080 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello {self.name}")
    
        
print(Student.class_year)

class Animal:
    def __init__(self,name):
        self.is_alive = True
        self.name = name
    def eating(self):
        print(f'{self.name} is eating')
    def sleep(self):
        print(f'{self.name} is sleeping')
    

class Dog(Animal):
    def speak(self):
        print('woof')

dog = Dog('Scooby Doo')

print(dog.speak())
        