n = int(input())

# Please write your code here.
answer = 0
cnt = 0
def backtracking(path):
    global cnt
    global answer
    if answer > n:
        return
    elif answer == n:
        cnt += 1
        return
    
    for i in range(1,5):
        answer += i
        backtracking(answer)
        answer -= i

backtracking(0)
print(cnt)