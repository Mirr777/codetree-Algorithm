N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.

dp = [float("inf")] * (M+1)
dp[0] = 0
for i in range(1,M+1):
    for j in range(N):
        if i >= coin[j]:
            if dp[i-coin[j]] == float("inf"): continue
            dp[i] = min(dp[i] , dp[i-coin[j]] + 1)

if dp[M] == float("inf"):
    dp[M] = -1

print(dp[M])