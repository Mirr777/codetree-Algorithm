n = int(input())

# Please write your code here.
from collections import deque
q = deque()
for i in range(1,n+1):
    q.append(i)

while len(q) != 1:
    q.popleft()
    a = q.popleft()
    q.append(a)

print(*q)