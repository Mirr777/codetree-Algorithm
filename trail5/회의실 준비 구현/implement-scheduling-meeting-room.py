n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
meetings.sort(key = lambda x : x[1])
a = -1
answer = 0
for x, y in meetings:
    if x >= a:
        a = y
        answer += 1
print(answer) 