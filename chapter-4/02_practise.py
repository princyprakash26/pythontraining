#display marks in sorted manner

a=int(input("enter the mark of the students n1: "))
b=int(input("enter the mark of the students n2: "))
c=int(input("enter the mark of the students n3: "))
d=int(input("enter the mark of the students n4: "))
e=int(input("enter the mark of the students n5: "))
f=int(input("enter the marks of the students n6: "))

marklist=[a,b,c,d,e,f]

marklist.sort()

marklist.reverse()
print(marklist)