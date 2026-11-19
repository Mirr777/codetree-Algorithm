n = int(input())

# Please write your code here.
dp = [0] * (n+1)
coin = [1,2,5]
dp[0] = 0

for i in range(n+1):
    for j in range(3):
        if  i >= coin[j]:
            dp[i] += dp[i-coin[j]] + 1

print((dp[-1] - dp[-2])%10007)
