

a=9
print(a)
def function():
    global a
    a=8
    print(a)
    a=900
    print(a)


# print(a)
function()
print(a)