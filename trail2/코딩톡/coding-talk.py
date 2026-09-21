n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# Please write your code here.
stack = []
people = []
for i in range(n):
    people.append(chr(i+65))
for i in range(p-1,m):
    stack.append(c[i])

for i in range(m):
    if u[i] == u[p-1]:
        stack.append(c[i])

if u[p-1] == 0:
    people = []
answer = []
for i in people:
    if i not in stack:
        answer.append(i)
print(*answer)

