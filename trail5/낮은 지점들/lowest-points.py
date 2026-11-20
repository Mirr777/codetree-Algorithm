n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

d = dict()
answer = 0

for i in range(n):
    if points[i][0] not in d:
        d[points[i][0]] = points[i][1]
        answer += points[i][1]
    else:
        if d[points[i][0]] > points[i][1]:
            answer -= d[points[i][0]]
            d[points[i][0]] = points[i][1]
            answer += d[points[i][0]]

print(answer)