import heapq
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
result = []
MAP = [[0] * n for _ in range(n)]
for i in range(m):
    MAP[edges[i][0]-1][edges[i][1]-1] = edges[i][2]

def dijstra(start):
    global result
    n = len(MAP)
    result = [float("inf")] * n
    result[start] = 0
    pq = [(0,start)]

    while pq:
        price, now = heapq.heappop(pq)

        if result[now] < price: continue
        
        for i in range(n):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i]
            price_sum = price + next_price
            if result[i] > price_sum:
                result[i] = price_sum
                heapq.heappush(pq, (price_sum, i))
    return

dijstra(0)
for i in range(1,len(result)):
    if result[i] != float("inf"):
        print(result[i])
    else:
        print(-1)