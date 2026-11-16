n = int(input())
x1, x2 = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x1.append((a,b))

# Please write your code here.

dp = [0] * n
x1.sort(key = lambda x : x[1])
dp[0] = 1
for i in range(n):
    for j in range(i):
        if x1[j][1] < x1[i][0]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))