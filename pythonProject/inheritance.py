# inheritance : allows classes(child) to inherit attributes and methods from another class(base)
# baseclass (parent class) subclass (Children)
# class A -> aB aC methods  ->  class B(inherits from A) -> bA bb aB aC methods in class A / methods
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,brand,make):
        self.brand = brand
        self.make = make

    @abstractmethod
    def printReg(self,regNo):
        pass

    def display_vehicle(self):
        print(self.brand,self.make)

class Toyota(Vehicle):
    def __init__(self,brand,make,speed,year):
        super().__init__(brand,make) #inheriting attributes from vehicle
        self.speed = speed
        self.year = year

    def display_toyota(self):
        return f"{self.brand} {self.make} {self.speed} {self.year}"

    def printReg(self,regNo):
        return f"{regNo}"


car1 = Toyota("Camry", "Toyota" , "200" , "2020")
print(car1.display_toyota())
print(car1.display_vehicle())
print(car1.printReg("KBC123"))