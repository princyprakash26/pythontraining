def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print('*',end='')
        print('\n')
pattern(3)

