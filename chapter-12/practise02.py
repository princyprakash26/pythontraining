
l1=[1,2,3,4,5,6,7,8,9,10]

for index,item in enumerate(l1):
    if (index+1==3 or index+1==5 or index+1==7):
        print(f"The Item number in {index} is {item}")