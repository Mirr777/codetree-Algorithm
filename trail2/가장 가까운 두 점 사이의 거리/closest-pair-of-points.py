n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
min_answer = float("inf")
for i in range(n):
    for j in range(i+1,n):
        if i == j: continue
        answer = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1]) ** 2
        min_answer = min(answer, min_answer)
print(min_answer)