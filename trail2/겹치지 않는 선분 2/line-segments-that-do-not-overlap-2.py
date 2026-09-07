n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = set()
for i in range(n):
    for j in range(i+1, n):
        if (lines[i][0] <= lines[j][0] and lines[i][1] >= lines[j][1]) or (lines[i][0] >= lines[j][0] and lines[i][1] <= lines[j][1]):
            answer.add(i)
            answer.add(j)
cnt = len(answer)
print(n-cnt)
    