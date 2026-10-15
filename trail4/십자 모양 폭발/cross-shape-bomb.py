n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
dx = [0,0,1,-1]
dy = [1,-1,0,0]

N = grid[r-1][c-1]

for i in range(n):
    for j in range(n):
        for k in range(N):
            for l in range(4):
                if i == r-1 + dy[l] * k and j == c-1 + dx[l] * k:
                    grid[i][j] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i-1 >=0 and grid[i][j] == 0 and grid[i-1][j] != 0:
                grid[i][j] = grid[i-1][j]
                grid[i-1][j] = 0 

for i in range(n):
    print(*grid[i])

