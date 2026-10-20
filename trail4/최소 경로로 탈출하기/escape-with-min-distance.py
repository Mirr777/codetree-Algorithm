from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def snake(n,m,a):
    q = deque()
    visited = []
    q.append((0,0))
    visited.append((0,0))

    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    dist = [[-1]*m for _ in range(n)]

    while q:
        y, x = q[0][0], q[0][1]
        q.popleft()
        for i in range(4):
            now_y = y + dy[i]
            now_x = x + dx[i]
            if 0 <= now_y < n and 0<= now_x < m:
                if (now_y, now_x) in visited: continue
                if a[now_y][now_x] == 1:
                    if now_y == n-1 and now_x == m-1:
                        return dist[y][x] + 2
                    visited.append((now_y,now_x))
                    q.append((now_y,now_x))
                    dist[now_y][now_x] = dist[y][x] + 1
    return -1 

print(snake(n,m,a))