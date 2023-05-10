


class Employee():
    name='sarano'     #A class attribute
    age=34
    grade='good'  

    def printObj(self):           
        print(f"the name is {self.name}")        

sarano=Employee()        # A basic object
shyam=Employee()         # A basic object
print(sarano.name)
print(shyam.name)                        
shyam.name='shyam'       #setting a instane attribute to shyam.
print(shyam.name)  
print(sarano.name)         
sarano.printObj()              
shyam.printObj()



