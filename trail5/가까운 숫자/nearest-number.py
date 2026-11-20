from sortedcontainers import SortedSet

n = int(input())
queries = list(map(int, input().split()))

# Please write your code here.

ss = SortedSet()
ss.add(0)
min_answer = float("inf")
for i in range(n):
    idx = ss.bisect_left(queries[i])
    if len(ss) == 1:
        min_answer = min(min_answer , queries[i])
    elif idx == 0:
        min_answer = min(min_answer, ss[1] - ss[0])
    elif idx == len(ss):
        min_answer = min(min_answer, queries[i]- ss[-1])
    else:
        min_answer = min(min_answer, ss[idx]-queries[i], queries[i]- ss[idx-1])
    ss.add(queries[i])
    print(min_answer)