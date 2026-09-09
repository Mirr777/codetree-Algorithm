A, B, C = map(int, input().split())

# Please write your code here.
a = C//A
b = C//B
max_answer = 0
for i in range(a+1):
    for j in range(b+1):
        answer = A*i + B*j
        if answer <= C:
            max_answer = max(max_answer, answer)
print(max_answer)