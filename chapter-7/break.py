
a=[1,2,3,4,5]

for item in a:
    print(item)
    if(item == 3):
        continue
    print("done this iteration for:",item)

print("the iteration for item is done")



a=[1,2,3,4,5]

for item in a:
    print(item)
    if(item == 3):
        break
    print("done this iteration for:",item)

print("the iteration for item is done")