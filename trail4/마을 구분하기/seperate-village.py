n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = []

x, y = 0,0

dxs = [0,0,1,-1]
dys = [1,-1,0,0]

def dfs(x,y):
    for i in range(4):
        if 0<=x + dxs[i] < n and 0 <= y + dys[i] < n:
            if grid[y + dys[i]][x+ dxs[i]] == 1 and (x+dxs[i], y+dys[i]) not in visited:
                visited.append((x+dxs[i], y+dys[i]))
                dfs(x+dxs[i], y+dys[i])
answer_list = []
answer = 0
cnt = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and (j,i) not in visited:
            visited.append((j,i))
            cnt+=1
            dfs(j,i)
            answer_list.append(len(visited)-answer)
            answer = len(visited)
print(cnt)
answer_list.sort()
for i in answer_list:
    print(i)
