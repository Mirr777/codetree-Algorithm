n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.


MAP = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    MAP[edges[i][0]][edges[i][1]] = 1
    MAP[edges[i][1]][edges[i][0]] = 1
visited = [0] * (n+1)
visited[1] = 1

path = []
def dfs(now):
    path.append(now)
    for i in range(n+1):
        if MAP[now][i] == 0:continue
        if visited[i] == 1:continue
        visited[i] = 1
        dfs(i)
dfs(1)
print(len(path)-1)