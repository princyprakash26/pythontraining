n=4
n=int(input("enter the value"))
for i in range(1,n+1):
    for j in range(i-n):
        print(" ",end="")
    for j in range(i-1+1):    
        print("*",end="")
    for j in range(i-n):
        print(" ",end="")
    print("\n",end="")


# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')    #another step
#     print(" ",end='')
#     print('\n',end='')