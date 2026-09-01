N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
answer = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if abs(k-c) <= 2:
                answer += 1 
            elif abs(j-b) <= 2:
                answer += 1
            elif abs(i-a) <= 2:
                answer += 1
print(answer)