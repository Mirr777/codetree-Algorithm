n = int(input())

# Please write your code here.
answer = 0
while True:
    if n < 0:
        answer = -1
        break
    if n % 5 == 0:
        answer += n //5
        break
    else:
        n -= 2
        answer += 1

print(answer)