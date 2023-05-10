# class creating calculator:
import math
class calculator():
    def __init__(self,number):
        self.number=number
    
    def square(self):
        return self.number*self.number
    def Squareroot(self):
        return math.sqrt(self.number)
    def cube(self):
        return self.number*self.number*self.number

two=calculator(4)
print(two.number)
print(two.cube())
print(two.square())
print(two.Squareroot())    