n = int(input("Enter number of fruits: "))
flist = []
print()
for i in range(n):
    f = input("Enter a fruit: ")
    w = input("Enter its weight: ")
    print()
    flist.append((f,w))
flist.sort()

for i in flist:
    print(i[0], ",", i[1], "lbs")
    print()

    


    
