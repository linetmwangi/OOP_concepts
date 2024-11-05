#inheritance:allows classes to inherit attributes and methods from another class
#baseclass (parent class) subclass (children)
#class A -> aB aC methods -> classB(inheritance from A) -> bA bb aB aC methods in class A / methods

from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand, make):
        self.brand= brand
        self.make = make

    @abstractmethod
    def printReg(self,regNo):
        pass

    def display_vehicle(self):
        print("Vehicle Name:", self.brand, self.make)

class Toyota(Vehicle):
    def __init__(self, brand, make):
        super().__init__(brand, make)
        self.speed = speed
        self.year = year

   def display_toyota(self):
       return f"{self.brand} {self.make} {self.year} "

   def printReg(self, regNo):
       return f"{regNo} "
