def fib(n):
    if n<= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
        
print("Enter number of terms")
print()

n = int(input())
print()

for i in range (n):
    print(fib(i))
    input()
