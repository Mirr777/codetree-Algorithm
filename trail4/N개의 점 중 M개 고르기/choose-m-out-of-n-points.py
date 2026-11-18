n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
path = []
min_answer = float("inf")
max_answer = 0
visit = []
def KFC(lev,start):
    global min_answer
    global max_answer
    if lev == m:        
        max_answer = 0
        for i in range(len(path)-1):
            for j in range(i+1,len(path)):
                answer = (path[i][0] - path[j][0]) ** 2 + (path[i][1] - path[j][1]) ** 2
                max_answer = max(max_answer, answer)
        visit.append(max_answer)
        
            
        
        return
    
    for i in range(start,n):
        path.append(points[i])
        KFC(lev+1,i+1)
        path.pop()
KFC(0,0)
print(min(visit))