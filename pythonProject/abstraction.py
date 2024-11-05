#hiding the complexity of data and exposing only what is necessary
#abc-abstract base classes : module in python that provides the infrastructure for defining absract base classes
#ABC's are a way of enforcing certain methods and properties in subclasses
#inheritance:allows classes to inherit attributes and methods from another class
#baseclass (parent class) subclass (children)
#class A -> aB aC methods -> classB(inheritance from A) -> bA bb aB aC methods in class A / methods

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display_message(self):
        return "this is an abstract class"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect=Rectangle(10, 20)
print(rect.area())
print(rect.perimeter())
print(rect.display_message())
