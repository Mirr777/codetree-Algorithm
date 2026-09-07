N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
cal = 0
answer = 0
P.sort()
for i in P:
    cal += i
    answer += 1
    if cal > B:
        cal = cal - (i//2)
        answer -= 1
        if cal > B:
            break
        else:
            answer +=1
print(answer)

