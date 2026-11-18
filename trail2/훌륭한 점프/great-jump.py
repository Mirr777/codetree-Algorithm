n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

visit = []
b = 0
visit.append(arr[0])
visit.append(arr[-1])
c = 0
while True:
    if c == 1: break
    if b + k + 1 == n: break
    a = float("inf")
    for j in range(b+1,b+k+1):
        if j == n:
            c = 1
            break
        if a >= arr[j]:
            a = arr[j]
            b = j
    visit.append(a)

print(max(visit))