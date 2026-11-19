n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
d = dict()
for i in range(n):
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1

for i in range(m):
    print(d.setdefault(nums[i], default = 0), end = " ")