n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
A = u
B = d
for i in range(t):
    A = [d[n-1]] + u[:n-1]
    B = [u[n-1]] + d[:n-1]
    u = A
    d = B
print(*A)
print(*B)