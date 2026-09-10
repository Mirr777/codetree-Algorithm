N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Please write your code here.
answer = 0
dart = [-1] * 101
answer_dart = [0] * 101
for i in range(N):
    if dart[pigeon[i]] == -1:
        dart[pigeon[i]] = position[i]
    elif dart[pigeon[i]] != position[i]:
        dart[pigeon[i]] = position[i]
        answer += 1
print(answer)