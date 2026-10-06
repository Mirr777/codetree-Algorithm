import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = []

dxs = [0,0,1,-1]
dys = [1,-1,0,0]

def dfs(x,y,k):
    global visited
    for l in range(4):
        if 0 <= x + dxs[l] < m and 0 <= y + dys[l] < n:
            if grid[y+dys[l]][x+dxs[l]] > k and (x+dxs[l],y+dys[l]) not in visited:
                visited.append((x+dxs[l], y + dys[l]))
                dfs(x+dxs[l], y + dys[l],k)

max_answer = 0
max_k = 1
def finding_number(n,m):
    global max_answer
    global max_k
    global visited
    for k in range(1,101):
        visited = []
        answer = 0
        for i in range(n):
            for j in range(m):
                if (j,i) not in visited and grid[i][j] > k:
                    visited.append((j,i))
                    answer += 1
                    dfs(j,i,k)
        if answer > max_answer:
            max_answer = answer
            max_k = k
finding_number(n,m)

print(max_k, max_answer)