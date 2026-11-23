n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

prefix = [float("-inf")] * (n)
answer = 0
for i in range(k):
    answer += arr[i]
    prefix[k-1] = answer 

for i in range(k, n):
    prefix[i] = prefix[i-1] - arr[i-k] + arr[i]

print(max(prefix))
