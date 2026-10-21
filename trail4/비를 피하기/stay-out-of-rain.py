from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dy = [0,0,1,-1]
dx = [1,-1,0,0]
new_grid = [[0] * n for _ in range(n)]
def BFS(n,grid,i,j):
    q = deque()
    visited = []
    dist = [[0] * n for _ in range(n)]
    q.append((i,j))
    while q:
        now_y, now_x = q[0][0] , q[0][1]
        q.popleft()
        for k in range(4):
            y = now_y + dy[k]
            x = now_x + dx[k]
            if 0 <= x < n and 0 <= y < n:
                if (y,x) in visited: continue
                if grid[y][x] == 1: continue
                if grid[y][x] == 3:
                    grid[i][j] == dist[y][x] + 1
                    new_grid[i][j] = dist[now_y][now_x] + 1
                    return
                visited.append((y,x))
                q.append((y,x))
                dist[y][x] = dist[now_y][now_x] + 1
    new_grid[i][j] = -1
    return

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            BFS(n,grid,i,j)
for i in range(n):
    print(*new_grid[i])