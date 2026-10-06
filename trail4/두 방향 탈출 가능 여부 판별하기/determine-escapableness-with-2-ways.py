n, m = map(int, input().split())  # n: 세로(행), m: 가로(열)
grid = [list(map(int, input().split())) for _ in range(n)]

# 2차원 방문 배열 생성 (False로 초기화)
visited = [[False] * m for _ in range(n)]

# 아래쪽(dy=1, dx=0), 오른쪽(dy=0, dx=1) 이동 방향 정의
# 관례적으로 y(행)를 앞에, x(열)를 뒤에 둡니다.
dys = [1, 0]
dxs = [0, 1]
answer = 0

def in_range(y, x):
    return 0 <= y < n and 0 <= x < m

def can_go(y, x):
    if not in_range(y, x):
        return False
    # 방문했거나 벽(0)인 경우 갈 수 없음
    if visited[y][x] or grid[y][x] == 0:
        return False
    return True

def dfs(y, x):
    global answer
    
    # 목적지(오른쪽 아래 끝)에 도달한 경우
    if y == n - 1 and x == m - 1:
        answer = 1
        return

    # 현재 위치 방문 처리
    visited[y][x] = True

    # 아래, 오른쪽 탐색
    for dy, dx in zip(dys, dxs):
        new_y, new_x = y + dy, x + dx
        if can_go(new_y, new_x):
            dfs(new_y, new_x)

# 시작점(0, 0)에서 탐색 시작
# 만약 시작점 자체가 벽(0)이라면 탐색을 진행하지 않습니다.
if grid[0][0] == 1:
    dfs(0, 0)

print(answer)