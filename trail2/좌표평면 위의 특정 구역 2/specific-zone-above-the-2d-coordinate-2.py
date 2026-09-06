n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
min_x = float("inf")
min_y = float("inf")
max_x = float("-inf")
max_y = float("-inf")
answer = 0
min_answer = float("inf")
for i in range(n):
    min_x = float("inf")
    min_y = float("inf")
    max_x = float("-inf")
    max_y = float("-inf")
    for j in range(n):
        if i == j:
            continue
        
        x1, y1 = points[j]
        if x1 < min_x:
            min_x = x1
        if x1 > max_x:
            max_x = x1
        if y1 < min_y:
            min_y = y1
        if y1 > max_y:
            max_y = y1
    answer = (max_y - min_y) * (max_x - min_x)
    min_answer = min(answer, min_answer)
print(min_answer)