n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
answer = 0
min_answer = float("inf")
arr.sort()
for i in range(n):
    answer = arr[i+n] - arr[i]
    min_answer = min(answer ,min_answer)
print(min_answer)
