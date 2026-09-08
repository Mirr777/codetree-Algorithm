n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.
max_answer = float("-inf")
for s in range(1001):
    answer = 0
    a = 0
    for i in range(n):
        if h[i] > s and a == 0:
            answer += 1
            a = 1
        elif h[i] <= s:
            a = 0
    max_answer = max(answer,max_answer)
print(max_answer)