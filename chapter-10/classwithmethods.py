# a very basic sample class

class Employee():
    name='princy'
    marks=34
    center='Tamilnadu'

    def printObj(self):
        print(f"the name is {self.name}")



harry=Employee()  #a basic object
shyam=Employee()  #a basic object
print(harry.marks)
print(harry.center)
print(harry.name)
harry.printObj()