"""
Employee payro;ll system
add an employee and add a salary on the same
return total cost on payroll
"""
"""
{
  "salary" : ,
  "name" " , 
}
"""
"""
  [ 
    {
  "salary" : ,
  "name" " , 
}, 
{
  "salary" : ,
  "name" " , 
},

  ]
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.name}, {self.salary})"


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self):
        return sum(employee.salary for employee in self.employees if employee.salary > 0)

payroll = Payroll()

emp1 = Employee("Joseph", 1000)
emp2 = Employee("Habiba", 2000)
emp3 = Employee("Bob", 40000)

payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.add_employee(emp3)

total_payroll = payroll.calculate_total_payroll()
print("Total Payroll:", total_payroll)

print("Employees:", payroll.employees)
