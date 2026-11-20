from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.

ss = SortedSet(arr)
for i in range(m):
    idx = ss.bisect_left(queries[i])
    if idx >= n:
        print(-1)
    else:
        print(ss[idx])