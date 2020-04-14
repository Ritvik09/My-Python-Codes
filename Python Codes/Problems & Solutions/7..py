bob = input("Enter phrase: ")
bob1 = ''
for i in range(0, len(bob)):
    if (bob[i].isalpha()):
        bob1 += bob[i].lower()

if(bob1 == bob1[::-1]):
    print()
    print("True")
else:
    print()
    print("False")
