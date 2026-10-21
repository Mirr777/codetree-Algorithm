from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.

dy = [-2,-2,-1,-1,1,1,2,2]
dx = [-1,1,-2,2,-2,2,-1,1]

q = deque()
visited = []
q.append((r1-1,c1-1))
visited.append((r1-1,c1-1))
dist = [[0] * n for _ in range(n)]


while q:
    now_y , now_x = q[0][0] , q[0][1]
    q.popleft()
    for i in range(8):
        y = now_y + dy[i]
        x = now_x + dx[i]
        if 0<= x < n and  0 <= y < n:
            if (y,x) in visited: continue
            visited.append((y,x))
            q.append((y,x))
            dist[y][x] = dist[now_y][now_x] + 1
if (r2-1,c2-1) in visited:
    print(dist[r2-1][c2-1])
else:
    print(-1)