N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
dp = [float("-inf")] * (M+1)
dp[0] = 0
for i in range(N):
    for j in range(M,-1,-1):
        if j >= w[i]:
            if dp[j-w[i]] == float("-inf"): continue
            dp[j] = max(dp[j], dp[j-w[i]] + v[i])
answer = 0
print(max(dp))