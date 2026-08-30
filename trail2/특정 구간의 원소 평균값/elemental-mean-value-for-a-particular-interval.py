n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import statistics
answer = 0
for i in range(n):
    for j in range(i+1,n+1):
        if statistics.mean(arr[i:j]) in arr[i:j]:
            answer +=1
print(answer)