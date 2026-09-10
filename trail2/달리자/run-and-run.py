n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
answer = 0
k = 0
for i in range(n):
    answer += (A[i]+k - B[i])
    k = (A[i]+ k - B[i])
print(answer)