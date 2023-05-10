
import random

number=random.randint(1,100)
guess=int(input('enter you Guessed number: '))
attempt=1

while(True):
    if(guess>number):
        guess=int(input('Guess the another number,the number you entered is too big: '))
        attempt+=1
    elif(guess<number):
        guess=int(input('Guess another number,the number you entered is too small:'))
        attempt+=1
    else:
        print(f'yes,you guessed the right number in {attempt} attempts:')
        break

