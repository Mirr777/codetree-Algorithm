n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
max_answer = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j ==k or k == i: continue
            if points[i][0] == points[j][0] and points[i][1] == points[k][1]:
                answer = abs((points[i][0]*points[j][1] + points[j][0]*points[k][1] + points[k][0]*points[i][1]) - (points[j][0]*points[i][1] + points[k][0]*points[j][1] + points[i][0] * points[k][1]))
                max_answer = max(max_answer, answer)
print(max_answer)