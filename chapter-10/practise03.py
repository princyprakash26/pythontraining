#create a class attribute with a.does change the class attribute.

class myclass():
    a=9

obj=myclass()

print(obj.a)

obj.a=0    #thus is setting an instance attributes.
print(obj.a)

myclass.a=0   #using this we can change the class attribute:

print(obj.a)


print(myclass.a)