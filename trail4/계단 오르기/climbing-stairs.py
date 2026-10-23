n = int(input())

# Please write your code here.

dp = [0] * (n + 3)
dp[2] = 1
dp[3] = 1

for i in range(4, n+ 1):
    if dp[i] !=0: continue
    dp[i] = dp[i-2] + dp[i-3]

print(dp[n]%10007)