N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
answer = 0
max_answer = float("-inf")
for j in range(-1,1002):
    answer = 0
    for i in range(N):
        if j < ranges[i][0]:
            answer += C
        elif ranges[i][0] <= j <= ranges[i][1]:
            answer += G
        elif j > ranges[i][1]:
            answer += H
    max_answer = max(answer, max_answer)

print(max_answer)