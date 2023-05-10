#multilevel inheritance:

class parent1():
    a=26

class child1(parent1):
    b=29
class child2(child1):
    c=10

ch=child2()

print(ch.a)
print(ch.b)
print(ch.c)