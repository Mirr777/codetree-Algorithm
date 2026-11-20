from sortedcontainers import SortedSet

n, m = map(int, input().split())
queries = list(map(int, input().split()))

# Please write your code here.

ss = SortedSet(x for x in range(1,m+1))

for i in range(n):
    idx = ss.bisect_left(queries[i])
    ss.remove(ss[idx])
    print(ss[-1])