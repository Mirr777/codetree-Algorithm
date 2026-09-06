n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
max_answer = 0
for i in range(n):
    for j in range(n-2):
        a = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        for k in range(n):
            for l in range(n-2):
                if (k == i) and abs(j-l)<3:
                    break
                else:
                    b = arr[k][l] + arr[k][l+1] + arr[k][l+2]
                    answer = a + b
                max_answer = max(answer, max_answer)
print(max_answer)
    