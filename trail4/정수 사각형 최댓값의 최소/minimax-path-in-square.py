n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [[float("inf")] * (n+1) for _ in range(n+1)]

dp[1][1] = grid[0][0]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j and i == 1: continue
        dp[i][j] = max(min(dp[i-1][j] , dp[i][j-1]) , grid[i-1][j-1])

print(dp[n][n])