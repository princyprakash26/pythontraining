#wipe out thr content
f=open('wipe.txt','a')
f.write('this is my name star')
f.close()

with open('wipe.txt','w') as f:
    f.write('')
