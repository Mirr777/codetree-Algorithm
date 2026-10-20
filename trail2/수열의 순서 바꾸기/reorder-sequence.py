n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
a = 0
answer = 0
for i in range(n):
    if a < sequence[i]:
        answer += 1
        a = sequence[i]
    else:
        answer = 1
        a = sequence[i]

new_answer = n - answer
if new_answer < 0:
    print(0)
else:
    print(new_answer)
