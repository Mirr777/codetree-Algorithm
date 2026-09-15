n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
while True:
    a = sorted(arr)
    if arr == a:
        break
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
print(*arr)