#x = heads
#y = legs
x = 35
y = 94

def solve(x,y):
    for i in range(x + 1):
        j = x - i
        if (2*i)+(4*j) == y:
            return i,j

solution = solve(x,y)
print(solution)
            
