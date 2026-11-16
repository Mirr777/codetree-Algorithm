n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [[float("-inf")] * m for _ in range(n)]

dp[0][0] = 1

for i in range(1,n):
    for j in range(1,m):
        max_num = 0
        for k in range(i):
            for l in range(j):
                if grid[i][j] <= grid[k][l]: continue               
                if dp[k][l] > max_num:
                    max_num = dp[k][l]
                    dp[i][j] = max_num + 1
answer = 0
for i in range(n):
    for j in range(m):
        if dp[i][j] > answer:
            answer = dp[i][j]
print(answer)