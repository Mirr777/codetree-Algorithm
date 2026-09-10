n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_answer = 0
min_answer = float("inf")
for i in range(51):
    for j in range(51):
        answer1, answer2, answer3, answer4 = 0, 0, 0, 0
        for k in range(n):
            if points[k][0] < 2*j and points[k][1] < 2*i:
                answer1 += 1
            elif points[k][0] > 2*j and points[k][1] < 2*i:
                answer2 += 1
            elif points[k][0] < 2*j and points[k][1] > 2*i:
                answer3 += 1
            elif points[k][0] > 2*j and points[k][1] > 2*i:
                answer4 += 1
        max_answer = max(answer1, answer2, answer3, answer4)
        min_answer = min(max_answer, min_answer)
print(min_answer)