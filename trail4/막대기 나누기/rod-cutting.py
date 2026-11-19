n = int(input())
profit = list(map(int, input().split()))

# Please write your code here.

dp = [float("-inf")] * (n+1)
dp[0] = 0

for i in range(n+1):
    for j in range(1,n+1):
        if i >= j:
            if dp[i-j] == float("-inf"): continue
            dp[i] = max(dp[i], dp[i-j] + profit[j-1])

print(max(dp))