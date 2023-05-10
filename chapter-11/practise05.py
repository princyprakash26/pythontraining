#using str method:

class vector2d:
    def __init__(self,i,j) -> None:
        self.i=i
        self.j=j
    def printvector(self):
        print(f'{self.i}i + {self.j}j')
class vector3d(vector2d):
    def __init__(self, i, j,k):
        super().__init__(i,j)
        self.k=k
    def printvector(self):
        print(f'{self.i}i + {self.j}j + {self.k}k')
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"


v3=vector3d(4,5,11)
print(v3)
