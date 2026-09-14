N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
arr.sort()
max_answer = 0
for i in range(N):
    answer = 0
    for j in range(i,N):
        if arr[i] +K >= arr[j]:
            answer +=1
    max_answer = max(answer,max_answer)
print(max_answer)
