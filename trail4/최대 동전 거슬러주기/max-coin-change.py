N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.

dp = [float("-inf")] * (M+1)
dp[0] = 0

for i in range(M+1):
    for j in range(N):
        if i >= coin[j]:
            if dp[i-coin[j]] == float("-inf"): continue
            dp[i] = max(dp[i],dp[i-coin[j]]+1)

if dp[-1] == float("-inf"):
    dp[-1] = -1
print(dp[-1])

