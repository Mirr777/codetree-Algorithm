N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
a = min(pos)
b = max(pos)
answer = 0
max_can = 0
for i in range(a,b+1):
    answer = 0
    for j in range(-K,K+1):
        for k, v in zip(candy, pos):
            if v == i+j:
                answer += k
    if answer > max_can:
        max_can = answer
print(max_can)