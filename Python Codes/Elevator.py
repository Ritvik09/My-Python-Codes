import time

m = 0

while True:

    n = int(input("Please enter floor number: "))
    print()
    
    if n > m:
        for f in range(m,n+1):
            time.sleep(2)
            print(f)
            print()

    elif m > n:
        for f in range(m,n-1,-1):
            time.sleep(2)
            print(f)
            print()

    if n == 1 or (n > 20 & n%10 == 1):
        a = "st"
    elif n == 2 or (n > 20 & n%10 == 2):
        a = "nd"
    elif n == 3 or (n > 20 & n%10 == 3):
        a = "rd"
    else:
        a = "th"
        
    print("You have reached " + str(n)+ a + " floor.")
    print()

    m = n
