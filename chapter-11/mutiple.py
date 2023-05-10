#multiple level

class parent1():
    a=26

class parent2():
    b=26
class child(parent1,parent2):
    c=10

ch=child()

print(ch.a)
print(ch.b)
print(ch.c)