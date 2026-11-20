from sortedcontainers import SortedSet

n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

ss = SortedSet(points)

for i in range(m):
    idx = ss.bisect_left(queries[i])
    if idx >= n:
        print(-1, -1)
    else:
        print(ss[idx][0], ss[idx][1])