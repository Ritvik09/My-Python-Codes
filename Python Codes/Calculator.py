# Print options (add,sub,mult,div)
# 1=add 2=sub 3=mult 4=div
# two inputs

while True:
    print("Welcome User!")
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")

    Operation = int(input())
    if Operation ==1:
        print("Enter two numbers:")
        Number_1 = float(input())
        print("+")
        Number_2 = float(input())
        total = Number_1 + Number_2
        print(total)

    elif Operation ==2:
        print("Enter two numbers:")
        Number_1 = float(input())
        print("-")
        Number_2 = float(input())
        total = Number_1 - Number_2
        print(total)

    elif Operation ==3:
        print("Enter two numbers:")
        Number_1 = float(input())
        print("*")
        Number_2 = float(input())
        total = Number_1 * Number_2
        print(total)

    elif Operation ==4:
        print("Enter two numbers:")
        Number_1 = float(input())
        print("/")
        Number_2 = float(input())
        if Number_2 == 0:
            print("Can't divide by zero")
        else:
            total = Number_1 / Number_2
            print(total)
             
        
    else:
        print("Invalid")

    print()

    print("Continue?")
    print("y for yes, n for no")
    ch = input()

    if ch =="n":
        break

    elif ch=="y":
        print()
        continue

        
