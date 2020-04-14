# create a dice 1-6

import random
import time

print("Welcome To Dice!")
while True:
    player = random.randint(1 , 6)
    print("You rolled a", player)
    ai = random.randint(1 , 6)
    print("The computer rolls....")
    time.sleep(3)
    print("The computer has rolled a", ai)
    
    if player > ai :
        print("You win!")
    elif player < ai :
        print("You lose!")
    else:
        print("It's a tie!")
    print()

    print("Continue?")
    print("y for yes, n for no")
    ch = input()

    if ch =="n":
        break  

    elif ch=="y":
            print()
            continue

    
