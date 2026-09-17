n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
happy = 0
for i in range(n):
    answer = 1
    for j in range(n-1):
        if grid[i][j] == grid[i][j+1]:
            answer +=1
        else:
            if answer >= m:
                happy += 1
                break
            answer = 1
    else:
        if answer >= m:
            happy += 1

for j in range(n):
    answer = 1
    for i in range(n-1):
        if grid[i][j] == grid[i+1][j]:
            answer +=1
        else:
            if answer >= m:
                happy += 1
                break
            answer = 1
    else:
        if answer >= m:
            happy += 1

print(happy)