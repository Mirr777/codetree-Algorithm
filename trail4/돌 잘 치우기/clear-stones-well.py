import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

# N: 격자 크기, K: 시작점 개수, M: 치울 돌의 개수
N, K, M = map(int, input().split())

grid = []
stones = []

for r in range(N):
    row = list(map(int, input().split()))
    grid.append(row)
    for c in range(N):
        if row[c] == 1:
            stones.append((r, c))

# 시작점 입력 (1-based index를 0-based index로 변환)
starts = []
for _ in range(K):
    r, c = map(int, input().split())
    starts.append((r - 1, c - 1))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    visited = [[False] * N for _ in range(N)]
    q = deque()
    count = 0
    
    # K개의 시작점을 모두 큐에 삽입
    for r, c in starts:
        if not visited[r][c]:
            visited[r][c] = True
            q.append((r, c))
            count += 1
            
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            # 격자 범위 내이고, 방문하지 않았으며, 돌이 없는(0) 경우
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    count += 1
                    
    return count

max_reachable = 0

# 전체 돌 중 M개를 뽑는 모든 조합 탐색
for selected_stones in combinations(stones, M):
    # 1. 선택한 M개의 돌 치우기
    for r, c in selected_stones:
        grid[r][c] = 0
        
    # 2. 도달 가능한 칸 수 계산 및 최댓값 갱신
    max_reachable = max(max_reachable, bfs())
    
    # 3. 치웠던 돌 원상복구
    for r, c in selected_stones:
        grid[r][c] = 1

print(max_reachable)