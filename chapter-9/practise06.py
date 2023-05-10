#logfile and find out whether it contains 'python:'

with open('logfile.txt','r') as f:
    f.read()
    if ('python' in f.read()):
       print('yes the file contain python')
    else:
        print("no,the file doesn't have python")
