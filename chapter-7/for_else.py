

a=[1,2,3,4,5]

for item in a:
    print(item)
    if(item == 3):
        continue
    print("done this iteration for:",item)
else:
    print("it is over now")
    print("the iteration for item is done")


# #incase it break else statement doesn't print anything.
# a=[1,2,3,4,5]

# for item in a:
#     print(item)
#     if(item == 3):
#         break
#     print("done this iteration for:",item)
# else:
#     print("we are done")             

print("the iteration for item is done")