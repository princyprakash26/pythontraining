#list of words to be censored:



with open('list.txt','r') as f:
    list=f.read()
    list=list.replace('donkey','CENSORED')
    list=list.replace('monkey','CENSORED')
    list=list.replace('buffalo','CENSORED')
    list=list.replace('cow','CENSORED')
with open('list.txt','w') as f:
    f.write(list)
    print('list.txt\n',list)
