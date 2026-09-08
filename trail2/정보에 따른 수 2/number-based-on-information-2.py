T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
answer = 0
for k in range(a,b+1):
    min_d1 = float("inf")
    min_d2 = float("inf")
    for t in range(T):
        if c[t] == "S":
            d1 = abs(x[t] - k)
            min_d1 = min(d1, min_d1)
        elif c[t] == "N":
            d2 = abs(x[t] - k)
            min_d2 = min(d2, min_d2)
    if min_d1 <= min_d2:
        answer += 1
print(answer)