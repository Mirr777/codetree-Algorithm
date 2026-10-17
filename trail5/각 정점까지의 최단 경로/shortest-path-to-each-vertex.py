import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

INF = float("inf")
dist = [INF] * (n + 1)
dist[k] = 0
pq = [(0, k)]

while pq:
    d, now = heapq.heappop(pq)
    if dist[now] < d:
        continue
    for nxt, w in graph[now]:
        nd = d + w
        if nd < dist[nxt]:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

for i in range(1, n + 1):
    print(dist[i] if dist[i] != INF else -1)