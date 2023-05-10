#letter format.

b=input("enter your name: ")
c=input("enter the date: ")

a=('''Dear,"name",
you are selected!
date''')

print(a.replace("name",b).replace("date",c))
