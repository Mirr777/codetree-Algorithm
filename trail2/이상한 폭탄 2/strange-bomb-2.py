N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
answer = -1
max_answer = -1
for i in range(N):
    if i + K + 1 >= N:
        b = N
    else:
        b = i+K+1
    for j in range(i+1, b):
        if num[i] == num[j]:
            answer = num[i]
        max_answer = max(max_answer, answer)
print(max_answer)