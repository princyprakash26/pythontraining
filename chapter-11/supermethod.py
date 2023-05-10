


class parent1():
    a=26
    def __init__(self) -> None:
        print('parent')

class child1(parent1):
    b=29
    def __init__(self) -> None:
        super().__init__()
        print('child1')
class child2(child1):
    c=10
    def __init__(self) -> None:
        # super().__init__()
        print('child2')

ch=child2()

print(ch.a)
print(ch.b)
print(ch.c)