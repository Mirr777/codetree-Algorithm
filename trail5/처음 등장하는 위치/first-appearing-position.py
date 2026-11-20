from sortedcontainers import SortedDict

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

sd = SortedDict()

for i in range(n):
    if arr[i] not in sd:
        sd[arr[i]] = i+1

for k, v in sd.items():
    print(k, v)