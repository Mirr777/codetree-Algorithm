n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.

path = []
visit = []
answer = 0
max_answer = 0
def backtracking(lev):
    global answer
    global max_answer
    dart = [0] * 1001
    for i in path:
        for j in range(i[0],i[1]+1):
            dart[j] += 1
    if max(dart) == 1:
        answer = len(path)
    max_answer = max(max_answer ,answer)
    if lev == n:
        return
    
    for i in range(n):
        if i in visit:continue
        if visit:
            if i < max(visit):continue
        visit.append(i)
        path.append((x1[i],x2[i]))
        backtracking(lev+1)
        path.pop()
        visit.pop()

backtracking(0)
print(max_answer)