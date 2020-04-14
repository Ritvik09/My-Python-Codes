rows = int(input())
columns = int(input())
matrix = []
z = 0
count = 0
for i in range(rows):
    a = []
    for j in range(columns):
        a.append(int(input()))
    matrix.append(a)
    
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 0:
            z += 1
        else:
            count += 1

if z > count:
    print("Sparse")
else:
    print("Not sparse")
