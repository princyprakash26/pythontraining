#represent complex numbers.along with overloaded operators + and * 

class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self,obj):
        return complex(self.a+obj.a,self.b+obj.b)
c1=complex(10,5)
c2=complex(10,5)
c3=c1+c2
print(c3.a,c3.b)
