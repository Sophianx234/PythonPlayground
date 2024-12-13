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