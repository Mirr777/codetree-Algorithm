from sortedcontainers import SortedSet

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ss = SortedSet(arr)

for i in range(1,k+1):
    print(ss[-i], end = " ")