#print sum of the first n numbers:

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
a=sum(5)
print(a)


