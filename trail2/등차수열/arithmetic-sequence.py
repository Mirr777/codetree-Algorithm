n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()
max_answer = float("-inf")
for k in range(101):
    answer = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if k - a[i] == a[j] - k:
                answer += 1
    max_answer = max(answer,max_answer)
print(max_answer)