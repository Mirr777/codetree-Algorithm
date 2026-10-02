n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
path = []
used = [0] * (n+1)
max_answer = 0
def permutation(lev):
    global max_answer
    if lev == n:
        answer = 0
        cnt = 0
        for i in path:
            answer += grid[cnt][i]
            cnt += 1
        max_answer = max(max_answer, answer)
        return 
    

    for i in range(n):
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(i)
        permutation(lev+1)
        path.pop()
        used[i] = 0

permutation(0)
print(max_answer)