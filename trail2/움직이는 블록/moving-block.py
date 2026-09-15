n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
a = sum(blocks)
b = a// n
answer = 0
for i in blocks:
    if i > b:
        answer += i-b
print(answer)