n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dx = [[(1,0),(2,0),(-1,0),(-2,0)],[(1,0),(-1,0),(0,1),(0,-1)],[(1,1),(1,-1),(-1,1),(-1,-1)]]
path = []

def finding(n,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                path.append((i,j))
    return

finding(n,grid)

visit = []
answer = len(path)
max_answer = 0
def KFC(lev,path):
    global answer
    global max_answer
    if lev == len(path):
        for i in list(set(visit)):
            if i not in path:
                answer +=1
        max_answer = max(answer, max_answer)
        answer = len(path)
        return

    for i in range(3):
        cnt = 0
        for j in range(4):
            if 0 <= path[lev][0] + dx[i][j][0] < n and 0 <= path[lev][1] + dx[i][j][1] < n:
                visit.append((path[lev][0] + dx[i][j][0], path[lev][1] + dx[i][j][1]))
                cnt +=1
        KFC(lev+1,path)
        for k in range(cnt):
            visit.pop()
    
KFC(0,path)
print(max_answer)