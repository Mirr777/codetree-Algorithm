n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
max_answer = 0
for i in range(n+1):
    answer = 0
    a = i
    for j in range(m):
        answer += arr[a]
        a = arr[a]
    max_answer = max(answer, max_answer)
print(max_answer)