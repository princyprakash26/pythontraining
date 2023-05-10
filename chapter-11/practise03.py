#class employee and add salary and increment.

class Employee():
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
    @property
    def salaryafterincrement(self):
        print (self.salary*(1 +self.increment))
    @salaryafterincrement.setter
    def salaryafterincrement(self):
        self.salary=self.salary*(1 +self.increment)

emp=Employee(11000,0.1)
# print(emp.salaryafterincrement)
# emp.salaryafterincrement*11000


