#@property

class Employee:
    a=10
    b=4
    c=6
    @classmethod
    def setattrs(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c

    @property        #without this the length doesn't work as property:
    def length(self):
        return self.a
    @length.setter             #setter
    def length(self,value):
        self.a=value

emp=Employee()
emp.setattrs(1,2,3)
print(emp.length)
emp.length=78
print(emp.length)