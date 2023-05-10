# copy of a text file 'ps.txt'

with open('ps.txt','r') as f:
    t=f.read()

with open('new.txt','w') as f:
    f.write(t)
    print(t)