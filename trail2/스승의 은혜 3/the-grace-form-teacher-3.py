N, B = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
max_answer = 0
for i in range(N): 
    new_gifts = gifts
    new_gifts[i][0] = new_gifts[i][0] // 2
    arr = []
    for j in range(N):
        arr.append(sum(gifts[j]))
    arr.sort()
    answer = 0
    real_answer = 0
    for k in range(N):
        answer += arr[k]
        real_answer += 1
        if answer > B:
            real_answer -=1
        max_answer = max(real_answer, max_answer)
    new_gifts[i][0] = new_gifts[i][0] * 2
print(max_answer)