board = [list(input()) for _ in range(10)]

# Please write your code here.
for i in range(10):
    for j in range(10):
        if board[i][j] == "L":
            a, b = i, j
        elif board[i][j] == "R":
            c, d = i, j
        elif board[i][j] == "B":
            e, f = i, j
if (a == c and a == e) and (b < d < f or f < d < b):
    answer = abs(f-b) + 1
elif b == d and b == f and (a < c < e or e < c < a):
    answer = abs(e-a) + 1
else:
    answer = abs(e -a) + abs(f - b)  -1
print(answer)