# Design guessing game using While loop

import random
print("Please Enter a highest Number")
highest = int(input())
answer = random.randint(1,highest)
print(highest)
print(answer)
print("please enter a number between 1 and {}".format(highest))
guess = 0
while answer != guess:
    guess = int(input())
    if guess == answer:
        print("You have guessed it correct")
        break
    else:
        if guess > answer:
            print("Please guess Lower")
        else:
            print("Please guess higher")


