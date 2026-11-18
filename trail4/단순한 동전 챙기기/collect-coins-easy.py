n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
dp = []

for p in range(1,10):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == str(p):
                dp.append((i,j))
            elif grid[i][j] == "S":
                start_point = (i,j)
            elif grid[i][j] == "E":
                end_point = (i,j)

path = []
path.append(start_point)
min_distance = float("inf")

def KFC(lev,start):
    global min_distance
    if lev == 3:
        path.append(end_point)
        dist = 0
        for i in range(4):
            dist += abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1])
        min_distance = min(dist, min_distance)
        path.pop()
        return
    
    for i in range(start, len(dp)):
        path.append(dp[i])
        KFC(lev+1, i+1)
        path.pop()

KFC(0,0)
if min_distance == float("inf"):
    min_distance = -1
print(min_distance)