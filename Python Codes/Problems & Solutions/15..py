blah = int(input("Enter number of people: "))
print()
blist = []

for i in range(blah):
    n = input("Enter name: ")
    a = input("Enter age: ")
    h = input("Enter height: ")
    blist.append((n,a,h))
    print()

blist.sort()

for i in range(blah):
    print(blist[i])
    print()
