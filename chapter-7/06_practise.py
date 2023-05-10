#factorial

n=5
fact=1
num=1
for i in range(n):
    fact=fact*num
    num=num+1

print(f"factorial of number {n} is {fact}")