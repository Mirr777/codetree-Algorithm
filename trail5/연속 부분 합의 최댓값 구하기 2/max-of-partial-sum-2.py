n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
answer = 0
max_answer = float("-inf")
if max(a) < 0:
    print(max(a))
else:
    for i in a:
        answer += i
        max_answer = max(answer, max_answer)
        if answer < 0:
            answer = 0
    print(max_answer)