from collections import deque

n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

q = deque()
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]
q.append((r-1,c-1))
dis = [[0] *n for _ in range(n)]
max_answer = 0
while q:
    y, x = q[0][0], q[0][1]
    dir = move_dir[y][x]-1
    q.popleft()
    for i in range(1,n):
        if 0 <= dy[dir]*i + y < n and 0 <= dx[dir]*i + x < n:
            if num[dy[dir]*i + y][dx[dir]*i + x] > num[y][x]:
                q.append((dy[dir]*i + y, dx[dir]*i + x))
                dis[dy[dir]*i + y][dx[dir]*i + x] = dis[y][x] + 1
                if dis[dy[dir]*i + y][dx[dir]*i + x] > max_answer:
                    max_answer = dis[dy[dir]*i + y][dx[dir]*i + x]
print(max_answer)