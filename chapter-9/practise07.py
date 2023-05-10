#find out the number line of python:

linenum = 1
with open('logfile.txt', 'r') as f:
    for line in f:
        if 'python' in line:
            text = f'line num {linenum}:{line}'
            print(text)
        linenum += 1

