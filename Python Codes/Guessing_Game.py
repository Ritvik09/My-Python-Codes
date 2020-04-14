# number guessing game

import random
import time

print("Welcome To The Higher or Lower Game!")
time.sleep(0.5)

while True:
    print("I'm thinking of a number between 1 and 100, try to guess it.")
    print("You have 6 attempts.")
    print()
    num = random.randint(1, 100)
    numGuesses = 1
    while True:
        print("Guess the number:")
        i = int(input())

        if i == num:
            print("Congratulations, you win!")
            break
        elif i > num:
            print("Go Lower")
            numGuesses += 1
            if numGuesses > 6:
                print()
                print("You lose. Better luck next time.")
                break
            elif numGuesses<= 6:
                time.sleep(1)
            print()
            continue
                

        elif i < num:
            print("Go Higher")
            numGuesses += 1
            if numGuesses > 6:
                print()
                print("You lose. Better luck next time.")
                break
            elif numGuesses<= 6:
                time.sleep(1)
            print()
            continue

    print()
    print("Continue?")
    print("y for yes, n for no")

    ch = input()

    if ch == "y":
        print()
        continue

    elif ch == "n":
        break
        
    
        
