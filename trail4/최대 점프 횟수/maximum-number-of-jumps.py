n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

dp = [0] * n

for i in range(1,n):
    for j in range(i):
        if i - j <= arr[j]:
            dp[i] = max(dp[i] , dp[j] + 1)
new_n = n
for i in range(1,n):
    if dp[i] == 0:
        new_n = i
        break
print(max(dp[:new_n +1]))