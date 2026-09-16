n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n-1):
    min_val = arr[i]
    for j in range(i+1,n):
        if min_val > arr[j]:
            min_val = arr[j]
            k = j
        else: continue
        arr[k], arr[i] = arr[i], arr[k]
       
print(*arr)