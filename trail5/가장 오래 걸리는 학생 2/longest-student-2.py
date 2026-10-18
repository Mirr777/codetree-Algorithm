import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

rev = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, price = map(int, input().split())
    rev[b].append((a, price))  # 방향 뒤집기

dist = [float("inf")] * (n + 1)
dist[n] = 0
pq = [(0, n)]

while pq:
    cost, now = heapq.heappop(pq)
    if dist[now] < cost:
        continue
    for nxt, w in rev[now]:
        nc = cost + w
        if nc < dist[nxt]:
            dist[nxt] = nc
            heapq.heappush(pq, (nc, nxt))

# 1 ~ n-1 중 최댓값
print(max(dist[1:n]))