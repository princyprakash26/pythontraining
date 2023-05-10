# class vector representing a vector of n dimension:

class vector:
    def __init__(self,l1) -> None:
        # self.dim=len(l1)
        self.l1=l1
    def __add__(self,obj):
        mylist=[]
        for i in range(len(obj.l1)):
            mylist.append(obj.l1[i]+self.l1[i])
        return vector(mylist)
    def __mul__(self,obj):
        dot=0
        for i in range(len(obj.l1)):
            dot+=(obj.l1[i]*self.l1[i])
        return dot
v1=vector([1,2])
v2=vector([11,12])
v3=v1+v2
v4=v1*v2
print(v3.l1)
print(v4)
    