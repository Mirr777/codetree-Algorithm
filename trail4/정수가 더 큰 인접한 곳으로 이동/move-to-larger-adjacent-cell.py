n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.

dy = [-1,1,0,0]
dx = [0,0,-1,1]
now_y =r
now_x = c
while True:
    A = a[now_y][now_x]
    print(A, end = " ")
    for i in range(4):
        y = now_y + dy[i]
        x = now_x + dx[i]
        if 0 <= y <= n and 0 <= x <= n:
            if a[y][x] > A:
                now_y = y
                now_x = x
                break
    else:
        break
    