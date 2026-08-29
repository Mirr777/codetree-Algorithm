N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
sum_num = sum(arr)
val = float("inf")
a = 0
for i in range(N):
    for j in range(i+1,N):
        a = abs(S - (sum_num - (arr[i]+arr[j])))
        val = min(val, a)
print(val)
