n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
distance = 0
checkpoint = 0
min_checkpoint = float("inf") 
for i in range(1,n-1):
    x = [p[0] for p in points] 
    y = [p[1] for p in points]
    x.pop(i)
    y.pop(i)
    distance = 0
    for j in range(n-2):
        distance += (abs(x[j] - x[j+1]) + abs(y[j]- y[j+1]))
    min_checkpoint = min(min_checkpoint, distance)
print(min_checkpoint)