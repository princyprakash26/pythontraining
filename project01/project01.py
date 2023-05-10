import random


def swg(comp,mine):
    if (comp==mine):
        return None
    if(comp=='snake' and mine=='gun'):
        return  True
    elif(comp=='water' and mine=='snake'):
        return True
    elif(comp=='gun' and mine=='water'):
        return True
    else:
        return False



choice=('snake','water','gun')
comp=random.randint(0,2)
comp=choice[comp]
mine=input('enter your choice either snake , water , gun: ')

win=swg(comp,mine)
print(f"you chose {mine} and computer chose {comp}")
if win is None:
    print('match is draw')
if win:
    print("you win")
else:
    print('you lose')