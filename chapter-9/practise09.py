#check whether it matches with another file:

with open('ps.txt','r') as f:
    text=f.read()
with open('mine.txt','r') as f:
    t=f.read()
    if (text==t):
        print('Both are similar')
    else:
        print('not similar')