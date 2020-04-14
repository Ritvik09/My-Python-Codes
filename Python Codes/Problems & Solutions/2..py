for i in range(2000,3201):
    if ((i%7 == 0) & (i%5 != 0)):
        print(i, ",", end=" ")
        if i == 3199:
            print(i)
