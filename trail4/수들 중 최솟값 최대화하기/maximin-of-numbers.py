n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
path = []
visit = []
max_answer = float("-inf")
min_answer = float("inf")
def backtracking(lev):
    global max_answer
    global min_answer
    if lev == n:
        min_answer = min(path)
        max_answer = max(min_answer,max_answer)
        return

    
    for i in range(n):
        if i in visit: continue
        visit.append(i)
        path.append(grid[lev][i])
        backtracking(lev+1)
        visit.pop()
        path.pop()
backtracking(0)
print(max_answer)