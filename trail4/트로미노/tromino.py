n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dy1 = [0,0,0,0,1,2]
dx1 = [0,1,2,0,0,0]

dy2 = [0,1,1,0,0,1,0,0,1,1,0,1]
dx2 = [0,0,1,0,1,0,0,1,1,0,1,1]

max_answer1 = 0
max_answer2 = 0
max_answer3 = 0
max_answer4 = 0
max_answer5 = 0
max_answer6 = 0
 
for i in range(n):
    for j in range(m):
        answer1 = 0
        answer2 = 0
        for k in range(3):
            if 0<= i + dy1[k] <n and 0 <= j + dx1[k] < m:
                answer1 += grid[i + dy1[k]][j + dx1[k]]
        max_answer1 = max(answer1, max_answer1)
        
        
        for l in range(3,6):
            if 0<= i + dy1[l] <n and 0 <= j + dx1[l] < m:
                answer2 += grid[i + dy1[l]][j + dx1[l]]
        max_answer2 = max(answer2, max_answer2)

for i in range(n):
    for j in range(m):
        answer3 = 0
        answer4 = 0
        answer5 = 0
        answer6 = 0
        for k in range(3):
            if 0<= i + dy2[k] <n and 0<= j + dx2[k] < m:
                answer3 += grid[i + dy2[k]][j + dx2[k]]
        max_answer3 = max(answer3, max_answer3)
        for l in range(3,6):
            if 0<= i + dy2[l] <n and 0 <= j + dx2[l] < m:
                answer4 += grid[i + dy2[l]][j + dx2[l]]
        max_answer4 = max(answer4, max_answer4)
        for o in range(6,9):
            if 0<= i + dy2[o] <n and 0 <= j + dx2[o] < m:
                answer5 += grid[i + dy2[o]][j + dx2[o]]
        max_answer5 = max(answer5, max_answer5)
        for p in range(9,12):
            if 0<= i + dy2[p] <n and 0 <= j + dx2[p] < m:
                answer6 += grid[i + dy2[p]][j + dx2[p]]
        max_answer6 = max(answer6, max_answer6)


print(max(max_answer1, max_answer2, max_answer3, max_answer4, max_answer5, max_answer6))