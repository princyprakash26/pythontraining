
num=int(input("Enter the number:"))

mul=[i*num for i in range(1,11)]

print(mul)

with open("mul.txt",'w') as f:
    f.write(str(mul))