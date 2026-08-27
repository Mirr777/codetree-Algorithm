n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
answer = 0
min_answer = float("inf")
for i in range(n):
    answer = 0
    for idx, ele in enumerate(a):
        if i < idx:
            answer += ele * (idx-i)
        elif i > idx:
            answer += ele * (n+idx-i)
    min_answer = min(min_answer, answer)
print(min_answer) 



