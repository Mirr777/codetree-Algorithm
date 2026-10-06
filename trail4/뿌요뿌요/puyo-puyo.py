n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = []
dxs = [0,0,1,-1]
dys = [1,-1,0,0]

def dfs(x,y,k):
    global visited
    global answer
    for i in range(4):
        if 0 <= dxs[i] + x < n and 0 <= dys[i] + y < n:
            if grid[dys[i] + y][dxs[i] + x] == k and (dxs[i]+x, dys[i] + y) not in visited:
                answer +=1
                visited.append((dxs[i] +x, dys[i] + y))
                dfs(dxs[i] + x ,dys[i] + y,k)
 
max_answer = 0
cnt = 0
answer = 0
for k in range(1,100):
    visited = []
    for i in range(n):
        for j in range(n):
            answer = 1
            if (j,i) not in visited and grid[i][j] == k:

                visited.append((j,i))
                dfs(j,i,k)
            if answer >= 4:
                cnt +=1
            max_answer = max(answer,max_answer)

print(cnt, end = " ")
print(max_answer)