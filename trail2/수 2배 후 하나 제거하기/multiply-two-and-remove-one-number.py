n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
min_diff = float("inf")
for i in range(n):
    arr[i] *= 2
    for j in range(n):
        remain = []
        for k in range(n):
            if k != j:
                remain.append(arr[k])
        sum_diff = 0
        for l in range(n-2):
            sum_diff += abs(remain[l+1] - remain[l])
        min_diff = min(min_diff, sum_diff)
    arr[i] //= 2
print(min_diff)