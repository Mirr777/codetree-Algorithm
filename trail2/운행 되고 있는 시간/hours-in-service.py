n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
arr = [0] * 1001
min_a = 1001
for i in range(n):
    arr = [0] * 1001
    for j in range(n):
        if i == j: continue
        for k in range(times[j][0], times[j][1]):
            arr[k] += 1
    a = arr.count(0)
    min_a = min(min_a, a)
print(1001-min_a)