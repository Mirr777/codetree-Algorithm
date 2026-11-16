n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.
dp = [0] * n
jobs.sort(key = lambda x : x[1])
dp[0] = jobs[0][2]
for i in range(1,n):
    for j in range(i):
        if jobs[i][0] > jobs[j][1] and dp[i] < dp[j] + jobs[i][2]:
            dp[i] = dp[j] + jobs[i][2]
        elif dp[i] < jobs[i][2]:
            dp[i] = jobs[i][2]
print(max(dp))