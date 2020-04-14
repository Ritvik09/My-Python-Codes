#Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
a = input("Enter encoded message: ")
print()
a1 = ''
s = 13
for i in range(len(a)):
    if (a[i].islower()):
        a1 += chr((ord(a[i]) + s - 97) % 26 + 97)
    elif (a[i].isupper()):
        a1 += chr((ord(a[i]) + s - 65) % 26 + 65)
    else:
        a1 += a[i]

print("Encoded message is: " + a1)

