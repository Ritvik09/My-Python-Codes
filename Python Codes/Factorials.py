#factorials

while True:
    n = int(input("Enter a number to find its factorial: "))

    factorial = 1
    i = 1
    while i <= n:
        factorial = factorial * i
        i = i+1

    print("The factorial is", factorial)

    print()
    print("Continue?")
    print("y for yes, n for no")

    ch = input()

    if ch == "y":
            print()
            continue

    elif ch == "n":
            break



    
     

 
    
    
