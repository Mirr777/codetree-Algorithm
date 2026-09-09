n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.
# 돌 리스트 제작
stone = [0] * 4
max_answer = 0
for i in range(3):
    stone = [0] * 4
    stone[i+1] = 1
    answer = 0
    for j in moves:
        stone[j[0]] ,stone[j[1]] = stone[j[1]], stone[j[0]]
        if stone[j[2]] == 1:
            answer += 1
    max_answer = max(answer, max_answer)
print(max_answer)