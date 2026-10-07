from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
q = deque()
q.append((0,0))
visited = []
visited.append((0,0))

dxs = [0,0,1,-1]
dys = [1,-1,0,0]


while q:
    now = q[0]
    q.popleft()
    if now == (m-1, n-1):
        answer = 1
        break
    
    for i in range(4):
        if 0 <= now[1] + dys[i] < n  and 0 <= now[0] + dxs[i] < m:
            if a[now[1] + dys[i]][now[0] + dxs[i]] == 0: continue
            if (now[0] + dxs[i],now[1] + dys[i]) in visited: continue
            visited.append((now[0] + dxs[i],now[1] + dys[i]))
            q.append((now[0] + dxs[i],now[1] + dys[i]))

print(answer)

