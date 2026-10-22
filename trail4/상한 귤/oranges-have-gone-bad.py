from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dy = [0,0,1,-1]
dx = [1,-1,0,0]
visit = []
q = deque()
dist = [[-1] * (n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            q.append((i,j))
            dist[i][j] = 0
            visit.append((i,j))
while q:
    now_y, now_x = q[0][0], q[0][1]
    q.popleft()
    for i in range(4):
        x = now_x + dx[i]
        y = now_y + dy[i]
        if 0 <= x < n and 0 <= y < n:
            if (y,x) in visit: continue
            if grid[y][x] == 1:
                visit.append((y,x))
                q.append((y,x))
                dist[y][x] = dist[now_y][now_x] + 1

for i in range(n):
    for j in range(n):
        if dist[i][j] == -1 and grid[i][j] == 1:
            dist[i][j] = -2

for i in range(n):
    print(*dist[i])