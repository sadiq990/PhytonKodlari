from genericpath import isdir
import random
from tkinter import E

top_of_range = input("type a number: ")

if top_of_range.isdigit(): # isdigit() -----> reqemdirse True deilse False verir.
    top_of_range = int(top_of_range)


    if top_of_range <= 0:
        print('Please type a number larger than 0 next time')
        quit()
else:
    print('Please type a number larger than 0 next time')
    quit()



random_number = random.randint(0,top_of_range)

print(random_number)


while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please  type a number next time')
        continue 
    
    if user_guess == random_number:
        print("you won it")
        break
    else:
        print("you got it wrong")