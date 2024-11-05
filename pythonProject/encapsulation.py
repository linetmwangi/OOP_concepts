#refers to bundling data and methods that work on the dta in a single unit called class
class Employee:
    def __init__(self, __name, salary):
        self.name =(__name)
        self.salary = salary
        self.dateofreg="10-31-2024"

    def display_employee(self):
        return f"Employee Name: {self.name} , salary: {self.salary} : {self.dateofreg}"

    def update_salary(self, amount):
        if amount > 0:
            self.salary += amount
        else:
            print("Salary cannot be negative")

 #create an object
emp1 = Employee("John", 5000)
print(emp1.display_employee())
print(emp1.name)
emp1.__name="Alice A"
print(emp1.update_salary(10000))
print(emp1.display_employee())
