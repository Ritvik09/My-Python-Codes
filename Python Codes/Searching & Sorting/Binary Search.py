mlist = [0,2,3,8,9]
n = 9
start = 0
end = len(mlist) - 1
while start <= end:
    mid = (start+end)//2
    if mlist[mid] == n:
        print("Found")
        break
    else: 
        if n  > mlist[mid]:
            start = mid + 1
        else:
            end = mid - 1
