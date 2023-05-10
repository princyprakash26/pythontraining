#another method to read.
f=open("ps.txt","r")

text=f.readline()
print(text)
text=f.readline()
print(text)
text=f.readline()
print(text)

#readlines used to make it in list:

# text=f.readlines()
# print(text)
# f.close()