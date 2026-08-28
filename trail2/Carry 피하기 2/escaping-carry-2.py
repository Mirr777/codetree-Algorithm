n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
answer = -1
value = 0
count = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a = arr[i]
            b = arr[j]
            c = arr[k]
            count = a + b + c
            value = 0
            for m in range(5):
                value += (((a % 10) + (b % 10) + (c % 10))% 10) * (10 ** m)
                a = a // 10
                b = b // 10
                c = c // 10
            if count == value:
                answer = max(answer, value)

print(answer)