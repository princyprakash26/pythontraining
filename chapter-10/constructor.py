
class Employee():
    def __init__(self,name,marks,center):
        self.name=name
        self.marks=marks
        self.center=center
    def printObj(self):
        print(f'The name is {self.name}')
        print(f'The mark is {self.marks}')
        print(f'The center is {self.center}')
    # @staticmethod
    # def greet():
    #     print("Good Day")
    
haro=Employee('Haro',34,'Delhi')
hasini=Employee('Hasini',96,'Chennai')
haro.printObj()
hasini.printObj()
