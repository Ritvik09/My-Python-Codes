print("Enter amount of element in grams")
amt = float(input())

print("Enter atomic weight of element")
atw = float(input())

def num_atoms(amt,atw):
    n = 6.022*10**23 *(amt/atw)
    return n

print("Numbers of atoms are")
print (num_atoms(amt,atw))
