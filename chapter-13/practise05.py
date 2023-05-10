

from functools import reduce

def max(m,n):
    if m>n:
        return m
    return n

a=[1,2,3,4,5,5,6,7,80,10]
maxnum=reduce(max,a)
print(maxnum)