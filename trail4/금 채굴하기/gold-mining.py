n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_answer = 0
for i in range(n):
    for j in range(n):
        for o in range(2*n):
            answer = grid[i][j]
            for k in range(n):
                for l in range(n):    
                    if 0 < abs(i - k) + abs(j-l)<= o:
                        if grid[k][l] == 1:
                            answer += 1
            if o**2 + (o + 1) ** 2 > answer*m : continue
            max_answer = max(max_answer, answer)

print(max_answer)


