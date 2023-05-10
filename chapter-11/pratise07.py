#__len()__

class vector:
    def __init__(self,l1) -> None:
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
    def __len__(self):
        return len(self.l1)
v1=vector([1,2,4])
v2=vector([11,12,13])
v3=v1+v2
v4=v1*v2
print(v3.l1)
print(v4)
print(len(v3))

