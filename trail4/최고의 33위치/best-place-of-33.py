n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_answer = 0
if n <= 3:
    for i in range(n):
        for j in range(n):
            max_answer += grid[i][j]
else:
    for i in range(n-2):
        for j in range(n-2):
            answer = 0
            for k in range(3):
                for l in range(3):
                    answer += grid[i+k][j+l]
            max_answer = max(max_answer, answer)
print(max_answer)