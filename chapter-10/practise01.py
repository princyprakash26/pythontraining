#class programmer for storing informaation of few programmers:
class Programmer():
    def __init__(self,name,language):
        self.name=name
        self.language=language
harry=Programmer('harry','Java')
rohan=Programmer('rohan','python')


print(rohan.name,rohan.language)
print(harry.name)