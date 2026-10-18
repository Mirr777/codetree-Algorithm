N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
A = []
for i in range(N):
    A.append((w[i], v[i], v[i]/w[i]))
A.sort(key = lambda x : -x[2])
answer = 0
for x, y, z in A:
    if x < M:
        answer += z * x
        M -= x
    else:
        answer += y * M / x
        break
print(f"{answer:.3f}") 
