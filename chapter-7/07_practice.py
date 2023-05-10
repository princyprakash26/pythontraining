
n=int(input("enter the value "))
for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    # for j in range(n-i):
    #     print(" ",end="")
    print("\n",end="")