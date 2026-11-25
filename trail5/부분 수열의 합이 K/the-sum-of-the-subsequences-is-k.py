n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

pre_fix = [0] * n
answer = 0

pre_fix[0] = arr[0]
for i in range(1,n):
    pre_fix[i] = pre_fix[i-1] + arr[i]

for i in range(n):
    if pre_fix[i] == k:
        answer += 1
    for j in range(i):
        if pre_fix[i] - pre_fix[j] == k:
            answer += 1
print(answer)