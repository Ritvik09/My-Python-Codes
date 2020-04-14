wlist = []
a=input("Enter first word: ")
b=input("Enter second word: ")
c=input("Enter third word: ")
wlist.append(a)
wlist.append(b)
wlist.append(c)

for i in range(0,len(wlist)):
    lenw = len(wlist[i])
    wlist[i] = lenw
print(wlist)

def lenw(wlist):
    return len(wlist)
w_length = list(map(lenw,wlist))
print(w_length)
