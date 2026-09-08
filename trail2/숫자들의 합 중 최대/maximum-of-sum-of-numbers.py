X, Y = map(int, input().split())

# Please write your code here.
case = []
answer = 0
max_answer = float("-inf")
for i in range(X,Y+1):
    case = list(map(int, list(str(i))))
    answer = 0
    for j in range(len(case)):
        answer += case[j]
    max_answer = max(answer, max_answer)
print(max_answer)