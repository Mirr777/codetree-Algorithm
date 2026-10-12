n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visit = []
min_answer = float("inf")
def backtracking(answer,now):
    global min_answer
    if len(visit) == n-1:
        if grid[now][0] != 0:
            answer += grid[now][0]
        else:
            answer += float("inf")

        min_answer = min(answer, min_answer)
        return
    
    for i in range(n):
        if grid[now][i] == 0:continue
        if i in visit: continue
        if i == 0: continue
        visit.append(i)
        answer += grid[now][i]
        backtracking(answer,i)
        answer -= grid[now][i]
        visit.pop()

backtracking(0,0)
print(min_answer)