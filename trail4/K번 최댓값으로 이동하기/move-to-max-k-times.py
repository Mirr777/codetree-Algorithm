from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

y = r-1
x = c-1

dxs = [1,-1,0,0]
dys = [0,0,-1,1]

for j in range(k):
    q = deque()
    visited = [[0] * n for _ in range(n)]
    q.append((x,y))
    visited[y][x] = 1
    val = []
    while q:
        x1 = q[0][0]
        y1 = q[0][1]
        q.popleft()
        for i in range(4):
            if 0 <= x1 + dxs[i] < n and 0 <= y1 + dys[i] < n:
                if grid[y1+dys[i]][x1 + dxs[i]] >= grid[y][x]: continue
                if visited[y1 + dys[i]][x1 + dxs[i]] == 1: continue
                visited[y1 + dys[i]][x1 + dxs[i]] = 1
                q.append((x1 + dxs[i], y1 + dys[i]))
                val.append(grid[y1+dys[i]][x1+dxs[i]])
    if val == []:
        break
    max_val = max(val)
    for l in range(n):
        for m in range(n):
            if grid[l][m] == max_val and visited[l][m] == 1:
                x = m
                y = l
                max_val = float("inf")
print(y+1, x+1)

