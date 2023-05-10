#Demonstration of maps:

# square=lambda x:x*x
# l1=[1,2,3,4,5]
# c=map(square,l1)
# print(list(c))


# #Demonstration of filter:

# greater=lambda x: x>4
# a=[1,2,3,4,5,6,7,8,9,10]
# d=filter(greater,a)
# print(list(d))

#Demonstration for reduce:
from functools import reduce    #need to import reduce because the module is not worked: 
re=lambda x,y:x+y
s=[1,2,3,4,5]
a=reduce(re,s)
print(a)