n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = float("inf")
for i in range(n):
    min_a = float("inf")
    max_b = 0
    for j in range(n):
        if i == j:continue
        a = segments[j][0]
        b = segments[j][1]
        min_a = min(min_a,a)
        max_b = max(max_b,b)
    answer = min(max_b-min_a , answer)
print(answer)