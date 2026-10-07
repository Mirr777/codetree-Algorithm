from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
answer = 0
q = deque()
visited = []
for i in range(k):
    q.append(points[i])
    visited.append(points[i])
    answer +=1

dxs = [0,0,1,-1]
dys = [1,-1,0,0]


while q:
    now = q[0]
    q.popleft()
    for i in range(4):
        if 0 <= now[1] + dxs[i] -1 < n and 0 <= now[0] + dys[i] -1 < n:
            if grid[now[0] + dys[i] -1][now[1] + dxs[i]-1] == 1: continue
            if (now[0] + dys[i], now[1] + dxs[i]) in visited: continue
            visited.append((now[0] + dys[i], now[1] + dxs[i]))
            q.append((now[0] + dys[i], now[1] + dxs[i]))
            answer +=1

print(answer)


