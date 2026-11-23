n, k = map(int, input().split())
arr =[[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

pre_fix = [[0] * (n+1) for _ in range(n+1)]
new_arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        pre_fix[i][j] = pre_fix[i-1][j] + pre_fix[i][j-1] - pre_fix[i-1][j-1] + arr[i][j]


max_answer = float("-inf")

for i in range(k,n+1):
    for j in range(k,n+1):
        new_arr[i][j] = pre_fix[i][j] - pre_fix[i][j-k] - pre_fix[i-k][j] + pre_fix[i-k][j-k]
        if new_arr[i][j] > max_answer:
            max_answer = new_arr[i][j]

print(max_answer)
