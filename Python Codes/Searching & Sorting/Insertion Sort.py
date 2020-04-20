def inserSort(A):
    for i in range(1,len(A)):
        num = A[i]
        while i-1>=0:
            if num < A[i-1]:
                A[i] = A[i-1]
                A[i-1] = num
                i = i - 1
            else:
                break
    return A

B = list(map(int,input().split()))
print(inserSort(B))

