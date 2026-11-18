n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_answer = 0
def possible(a,b,c,d):
    for i in range(a,c+1):
        for j in range(b,d+1):
            if grid[i][j] <= 0:
                return False
    return True
for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                if possible(i,j,k,l):
                    answer = (abs(i-k)+1) * (abs(j-l)+1)
                    max_answer = max(max_answer, answer)
if max_answer == 0:
    max_answer = -1

print(max_answer)