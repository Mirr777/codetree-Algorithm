n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
a = n
for i in range(n-1,0,-1):
    for j in range(k-1,k+m-1):
        if grid[i][j] == 1:
            a = i
for l in range(k-1,k+m-1):
    grid[a-1][l] = 1
for i in range(n):
    print(*grid[i])
