n = int(input())
arr = list(input().split())

# Please write your code here.
answer = 0
while True:
    a = sorted(arr)
    if arr == a:
        break
    for i in range(n-1):
        if ord(arr[i]) > ord(arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            answer +=1

print(answer)