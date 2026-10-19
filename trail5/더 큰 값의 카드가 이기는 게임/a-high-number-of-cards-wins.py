
N = int(input())
B = [int(input()) for _ in range(N)]

# Please write your code here.

B.sort()
B.append(2*N+1)
answer = 0
a = 0
b = 0
for i in range(N):
    a = B[i+1] - B[i] - 1
    b += 1
    while True:
        if a == 0 or b ==0:
            break
        elif a > 0 and b >0:
            answer += 1
            a -= 1
            b -= 1

print(answer)