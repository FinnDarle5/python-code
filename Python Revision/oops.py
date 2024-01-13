class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        return self.salary

a = Employee("Ayush" , 182000)
print(a.name)
print(a.salary)

b = Employee("Aradhya", 18200000000)
# print(b.name)
# print(b.salary)

