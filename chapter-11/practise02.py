#Add a method bark to class dog
class Animals():
    def __init__(self,animal_type) -> None:
        self.animal_type=animal_type

class Pets(Animals):
    def __init__(self,animal_type,pet_type):
        super().__init__(animal_type)
        self.pet_type=pet_type
            
                 
class Dog(Pets):
    def __init__(self,animal_type,pet_type,dog):
        super().__init__(animal_type,pet_type)
        self.dog=dog
    def bark(self):
        print('It barks as Bow Bow')
ch=Dog('Dog','Pet','Husky')
print(f"my {ch.animal_type}is a {ch.pet_type} and is a type {ch.dog}")  
ch.bark()            
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 

                 
                 
                 
                 
                 

        

