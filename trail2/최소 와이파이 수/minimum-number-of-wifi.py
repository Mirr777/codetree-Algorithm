n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
a = 0
answer = 0
while True:
    if a >= n:
        break
    if arr[a] == 1:
        a = a + 2*m + 1
        answer += 1
    else:
        a += 1
print(answer)