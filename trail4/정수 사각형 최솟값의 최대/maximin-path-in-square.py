n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0] * (n+1) for _ in range(n+1)]

dp[1][1] = grid[0][0]
for i in range(n):
    for j in range(n):
        if dp[i+1][j] == 0 and dp[i][j+1] == 0:
            dp[i+1][j+1] = grid[i][j]
        elif dp[i+1][j] == 0:
            dp[i+1][j+1] = min(grid[i][j], dp[i][j+1])
        elif dp[i][j+1] == 0:
            dp[i+1][j+1] = min(grid[i][j],dp[i+1][j])
        elif dp[i+1][j] < dp[i][j+1]:
            dp[i+1][j+1] = min(grid[i][j],dp[i][j+1]) 
        elif dp[i+1][j] >= dp[i][j+1]:
            dp[i+1][j+1] = min(grid[i][j], dp[i+1][j])

print(dp[n][n])