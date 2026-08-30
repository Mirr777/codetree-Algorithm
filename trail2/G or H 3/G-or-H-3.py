n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
answer = 0
max_answer = float("-inf")
for i in range(n):
    answer = 0
    for j in range(k+1):
        if x[i]+j in x:
            a = x.index(x[i]+j)
            if c[a] == "G":
                answer += 1
            elif c[a] == "H":
                answer +=2
    if answer>max_answer:
        max_answer = answer
print(max_answer)